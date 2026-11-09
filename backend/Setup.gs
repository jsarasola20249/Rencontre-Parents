/**
 * Setup.gs — Crea el Sheet y la carpeta Identité una vez.
 * En el editor: ejecutar setupRencontre y autorizar.
 */

function setupRencontre() {
  var props = proprietes();
  var dossier = assurerDossier(props);
  assurerIdentite(props, dossier);
  var ss = assurerTableur(props, dossier);
  var hojas = [
    [FEUILLE_ENSEIGNANT, ENCABEZADOS_ENSEIGNANT],
    [FEUILLE_ELEVES, ENCABEZADOS_ELEVES],
    [FEUILLE_RENCONTRES, ENCABEZADOS_RENCONTRES],
    [FEUILLE_CHOIX, ENCABEZADOS_CHOIX]
  ];
  for (var i = 0; i < hojas.length; i++) {
    var sh = assurerFeuille(ss, hojas[i][0], hojas[i][1]);
    fijarTexto(sh, hojas[i][1].length);
  }
  ecrireCatalogue(ss);
  retirerFeuilleVide(ss);
  SpreadsheetApp.flush();
  var msg = 'Tableur prêt : ' + ss.getUrl() + '\nDossier : ' + dossier.getUrl();
  Logger.log(msg);
  return msg;
}

function assurerDossier(props) {
  var id = props.getProperty(PROP_DOSSIER_ID);
  if (id) {
    try {
      return DriveApp.getFolderById(id);
    } catch (e) {
      Logger.log('Dossier anterior ausente, se crea otro.');
    }
  }
  var dossier = DriveApp.createFolder(NOM_DOSSIER);
  props.setProperty(PROP_DOSSIER_ID, dossier.getId());
  return dossier;
}

function assurerIdentite(props, dossier) {
  var id = props.getProperty(PROP_IDENTITE_ID);
  if (id) {
    try {
      return DriveApp.getFolderById(id);
    } catch (e) {
      Logger.log('Dossier Identité ausente, se crea otro.');
    }
  }
  var identite = dossier.createFolder(NOM_IDENTITE);
  props.setProperty(PROP_IDENTITE_ID, identite.getId());
  return identite;
}

function assurerTableur(props, dossier) {
  var id = props.getProperty(PROP_SPREADSHEET_ID);
  if (id) {
    try {
      return SpreadsheetApp.openById(id);
    } catch (e) {
      Logger.log('Tableur anterior ausente, se crea otro.');
    }
  }
  var ss = SpreadsheetApp.create(NOM_TABLEUR);
  DriveApp.getFileById(ss.getId()).moveTo(dossier);
  props.setProperty(PROP_SPREADSHEET_ID, ss.getId());
  return ss;
}

function assurerFeuille(ss, nom, enTetes) {
  var sh = ss.getSheetByName(nom);
  if (!sh) sh = ss.insertSheet(nom);
  var ancho = enTetes.length;
  var actuales = sh.getRange(1, 1, 1, ancho).getValues()[0];
  var igual = true;
  for (var i = 0; i < ancho; i++) {
    if (String(actuales[i] || '') !== enTetes[i]) igual = false;
  }
  if (!igual) sh.getRange(1, 1, 1, ancho).setValues([enTetes]);
  sh.setFrozenRows(1);
  sh.getRange(1, 1, 1, ancho).setFontWeight('bold');
  return sh;
}

function fijarTexto(sh, columnas) {
  var filas = Math.max(sh.getMaxRows(), 2);
  sh.getRange(1, 1, filas, columnas).setNumberFormat('@');
}

function ecrireCatalogue(ss) {
  var cat = catalogueReferentiel();
  var titres = {};
  var noms = {};
  var grille = [['Section', 'Code', 'Force', 'Défi']];
  for (var s = 0; s < cat.grille.length; s++) {
    var sec = cat.grille[s];
    titres[sec.code] = sec.titre;
    for (var i = 0; i < sec.items.length; i++) {
      var item = sec.items[i];
      grille.push([sec.titre, item.code, item.force, item.defi]);
    }
  }
  var strategies = [['Code', 'Bloc', 'Nom', 'Comment l’utiliser', 'Exemple']];
  for (var j = 0; j < cat.strategies.length; j++) {
    var st = cat.strategies[j];
    noms[st.code] = st.nom;
    strategies.push([st.code, st.bloc, st.nom, st.utilisation, st.exemple]);
  }
  var liens = [['Section', 'Code section', 'Code stratégie', 'Nom']];
  for (var k = 0; k < cat.correspondance.length; k++) {
    var lien = cat.correspondance[k];
    liens.push([titres[lien.section] || lien.section, lien.section, lien.strategie, noms[lien.strategie] || lien.strategie]);
  }
  ecrireFeuilleCatalogue(ss, FEUILLE_GRILLE, grille);
  ecrireFeuilleCatalogue(ss, FEUILLE_STRATEGIES, strategies);
  ecrireFeuilleCatalogue(ss, FEUILLE_CORRESPONDANCE, liens);
}

function ecrireFeuilleCatalogue(ss, nom, lignes) {
  var sh = ss.getSheetByName(nom);
  if (!sh) sh = ss.insertSheet(nom);
  sh.clear();
  sh.getRange(1, 1, lignes.length, lignes[0].length).setValues(lignes);
  sh.setFrozenRows(1);
  sh.getRange(1, 1, 1, lignes[0].length).setFontWeight('bold');
  sh.getRange(1, 1, lignes.length, lignes[0].length).setNumberFormat('@');
  try {
    var protecciones = sh.getProtections(SpreadsheetApp.ProtectionType.SHEET);
    for (var i = 0; i < protecciones.length; i++) protecciones[i].remove();
    var protection = sh.protect();
    protection.setWarningOnly(true);
    protection.setDescription('Catalogue généré par setupRencontre.');
  } catch (e) {
    Logger.log('Protection non posée sur ' + nom);
  }
  return sh;
}

function retirerFeuilleVide(ss) {
  var nombres = ['Sheet1', 'Feuille 1'];
  for (var i = 0; i < nombres.length; i++) {
    var sh = ss.getSheetByName(nombres[i]);
    if (sh && ss.getSheets().length > 1) ss.deleteSheet(sh);
  }
}
