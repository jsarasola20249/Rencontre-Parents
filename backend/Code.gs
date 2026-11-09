/**
 * Code.gs — Web App de un solo enseignant.
 * La pantalla y los mensajes que ve están en francés.
 */

var FEUILLE_ENSEIGNANT = 'Enseignant';
var FEUILLE_ELEVES = 'Élèves';
var FEUILLE_RENCONTRES = 'Rencontres';
var FEUILLE_CHOIX = 'Choix';
var FEUILLE_GRILLE = 'Grille';
var FEUILLE_STRATEGIES = 'Stratégies';
var FEUILLE_CORRESPONDANCE = 'Correspondance';

var PROP_SPREADSHEET_ID = 'SPREADSHEET_ID';
var PROP_DOSSIER_ID = 'DOSSIER_ID';
var PROP_IDENTITE_ID = 'IDENTITE_ID';

var NOM_TABLEUR = 'Rencontre de parents';
var NOM_DOSSIER = 'Rencontre de parents';
var NOM_IDENTITE = 'Identité';
var ZONE = 'America/Toronto';

var ENCABEZADOS_ENSEIGNANT = ['Prénom', 'Nom', 'Courriel', 'Téléphone', 'École', 'Classe', 'Année scolaire'];
var ENCABEZADOS_ELEVES = ['ID', 'Prénom', 'Nom', 'Actif', 'Créé le'];
var ENCABEZADOS_RENCONTRES = [
  'ID',
  'ID élève',
  'Date de la rencontre',
  'Enregistré le',
  'Forces principales',
  'Défis prioritaires',
  'Objectif',
  'Commentaires',
  'Notes internes'
];
var ENCABEZADOS_CHOIX = ['ID rencontre', 'Section', 'Type', 'Code'];

function doGet() {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('Rencontre de parents')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/** Contexto inicial de la pantalla. */
function obtenirContexte() {
  return {
    aujourdHui: aujourdhuiTexte(),
    enseignant: obtenirEnseignant(),
    eleves: listerEleves(),
    catalogue: construireCatalogue()
  };
}

function proprietes() {
  return PropertiesService.getScriptProperties();
}

function exigerTableur() {
  var id = proprietes().getProperty(PROP_SPREADSHEET_ID);
  if (!id) {
    throw new Error('Exécutez setupRencontre dans l’éditeur Apps Script.');
  }
  try {
    return SpreadsheetApp.openById(id);
  } catch (e) {
    throw new Error('Le tableur est introuvable. Exécutez setupRencontre.');
  }
}

function feuille(nom) {
  var sh = exigerTableur().getSheetByName(nom);
  if (!sh) {
    throw new Error('La feuille « ' + nom + ' » est absente. Exécutez setupRencontre.');
  }
  return sh;
}

function texteCellule(valeur) {
  if (Object.prototype.toString.call(valeur) === '[object Date]') {
    return Utilities.formatDate(valeur, ZONE, 'yyyy-MM-dd');
  }
  return String(valeur == null ? '' : valeur).trim();
}

function horodatageCellule(valeur) {
  if (Object.prototype.toString.call(valeur) === '[object Date]') {
    return Utilities.formatDate(valeur, ZONE, 'yyyy-MM-dd HH:mm');
  }
  return String(valeur == null ? '' : valeur).trim();
}

function maintenantTexte() {
  return Utilities.formatDate(new Date(), ZONE, 'yyyy-MM-dd HH:mm');
}

function aujourdhuiTexte() {
  return Utilities.formatDate(new Date(), ZONE, 'yyyy-MM-dd');
}

function avecVerrou(fn) {
  var verrou = LockService.getScriptLock();
  verrou.waitLock(20000);
  try {
    return fn();
  } finally {
    verrou.releaseLock();
  }
}

function lireDonnees(nom) {
  var valeurs = feuille(nom).getDataRange().getValues();
  if (!valeurs || valeurs.length < 2) return [];
  var lignes = [];
  for (var i = 1; i < valeurs.length; i++) {
    if (String(valeurs[i][0] || '').trim() !== '') lignes.push(valeurs[i]);
  }
  return lignes;
}

function prochainId(prefixe, ids) {
  var max = 0;
  var re = new RegExp('^' + prefixe + '-(\\d+)$');
  for (var i = 0; i < ids.length; i++) {
    var m = re.exec(String(ids[i] || ''));
    if (m) max = Math.max(max, Number(m[1]));
  }
  var n = String(max + 1);
  while (n.length < 3) n = '0' + n;
  return prefixe + '-' + n;
}

function indexCatalogue() {
  var cat = catalogueReferentiel();
  var items = {};
  var titres = {};
  for (var s = 0; s < cat.grille.length; s++) {
    var sec = cat.grille[s];
    titres[sec.code] = sec.titre;
    for (var i = 0; i < sec.items.length; i++) {
      items[sec.code + '|' + sec.items[i].code] = true;
    }
  }
  var strategies = {};
  for (var j = 0; j < cat.strategies.length; j++) {
    strategies[cat.strategies[j].code] = cat.strategies[j];
  }
  var liens = {};
  for (var k = 0; k < cat.correspondance.length; k++) {
    var lien = cat.correspondance[k];
    liens[lien.section + '|' + lien.strategie] = true;
  }
  return {
    items: items,
    titres: titres,
    strategies: strategies,
    liens: liens,
    grille: cat.grille,
    correspondance: cat.correspondance
  };
}

/** Catálogo ya unido, listo para la pantalla. */
function construireCatalogue() {
  var index = indexCatalogue();
  var sections = [];
  for (var s = 0; s < index.grille.length; s++) {
    var sec = index.grille[s];
    var strategies = [];
    for (var k = 0; k < index.correspondance.length; k++) {
      var lien = index.correspondance[k];
      if (lien.section !== sec.code) continue;
      var strategie = index.strategies[lien.strategie];
      strategies.push({
        code: strategie.code,
        nom: strategie.nom,
        utilisation: strategie.utilisation,
        exemple: strategie.exemple,
        transversale: strategie.bloc === 'Stratégies transversales'
      });
    }
    sections.push({
      code: sec.code,
      titre: sec.titre,
      items: sec.items,
      strategies: strategies
    });
  }
  return { sections: sections };
}
