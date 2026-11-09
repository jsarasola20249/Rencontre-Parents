/**
 * RencontreService.gs — Fichas fechadas, historial y elecciones.
 */

function listerRencontres(data) {
  data = data || {};
  var eleveId = String(data.eleveId || '').trim();
  if (!eleveId) return [];
  var lignes = lireDonnees(FEUILLE_RENCONTRES);
  var liste = [];
  for (var i = 0; i < lignes.length; i++) {
    if (texteCellule(lignes[i][1]) !== eleveId) continue;
    liste.push({
      id: texteCellule(lignes[i][0]),
      eleveId: texteCellule(lignes[i][1]),
      date: texteCellule(lignes[i][2]),
      enregistreLe: horodatageCellule(lignes[i][3])
    });
  }
  liste.sort(function (a, b) {
    if (a.date !== b.date) return a.date < b.date ? 1 : -1;
    if (a.enregistreLe !== b.enregistreLe) return a.enregistreLe < b.enregistreLe ? 1 : -1;
    return a.id < b.id ? 1 : -1;
  });
  return liste;
}

function obtenirRencontre(data) {
  var id = String((data && data.id) || '').trim();
  if (!id) throw new Error('Cette rencontre est introuvable.');
  var valeurs = feuille(FEUILLE_RENCONTRES).getDataRange().getValues();
  for (var i = 1; i < valeurs.length; i++) {
    if (texteCellule(valeurs[i][0]) !== id) continue;
    return rencontreDepuisLigne(valeurs[i]);
  }
  throw new Error('Cette rencontre est introuvable.');
}

function rencontreDepuisLigne(ligne) {
  var id = texteCellule(ligne[0]);
  return {
    id: id,
    eleveId: texteCellule(ligne[1]),
    date: texteCellule(ligne[2]),
    enregistreLe: horodatageCellule(ligne[3]),
    forcesPrincipales: texteLibre(ligne[4]),
    defisPrioritaires: texteLibre(ligne[5]),
    objectif: texteLibre(ligne[6]),
    commentaires: texteLibre(ligne[7]),
    notesInternes: texteLibre(ligne[8]),
    choix: choixDe(id)
  };
}

/** No convierte en fecha un párrafo de la síntesis. */
function texteLibre(valeur) {
  if (Object.prototype.toString.call(valeur) === '[object Date]') {
    return Utilities.formatDate(valeur, ZONE, 'yyyy-MM-dd');
  }
  return String(valeur == null ? '' : valeur).replace(/^\s+|\s+$/g, '');
}

function choixDe(id) {
  var lignes = lireDonnees(FEUILLE_CHOIX);
  var out = [];
  for (var i = 0; i < lignes.length; i++) {
    if (texteCellule(lignes[i][0]) !== id) continue;
    out.push({
      section: texteCellule(lignes[i][1]),
      type: texteCellule(lignes[i][2]),
      code: texteCellule(lignes[i][3])
    });
  }
  return out;
}

function enregistrerRencontre(data) {
  return avecVerrou(function () {
    data = data || {};
    var eleveId = String(data.eleveId || '').trim();
    var date = String(data.date || '').trim();
    if (!eleveId) throw new Error('Choisissez un élève.');
    if (!trouverEleve(eleveId)) throw new Error('Cet élève est introuvable.');
    if (!dateValide(date)) throw new Error('Indiquez la date de la rencontre.');
    var index = indexCatalogue();
    var choix = normaliserChoix(data.choix, index);
    var sh = feuille(FEUILLE_RENCONTRES);
    var valeurs = sh.getDataRange().getValues();
    var id = String(data.id || '').trim();
    var quand = maintenantTexte();
    var ligne = [
      id,
      eleveId,
      date,
      quand,
      String(data.forcesPrincipales || '').trim(),
      String(data.defisPrioritaires || '').trim(),
      String(data.objectif || '').trim(),
      String(data.commentaires || '').trim(),
      String(data.notesInternes || '').trim()
    ];
    if (id) {
      var trouve = false;
      for (var i = 1; i < valeurs.length; i++) {
        if (texteCellule(valeurs[i][0]) !== id) continue;
        if (texteCellule(valeurs[i][1]) !== eleveId) {
          throw new Error('Cette rencontre appartient à un autre élève.');
        }
        ligne[0] = id;
        sh.getRange(i + 1, 1, 1, ligne.length).setValues([ligne]);
        trouve = true;
        break;
      }
      if (!trouve) throw new Error('Cette rencontre est introuvable.');
    } else {
      var ids = [];
      for (var j = 1; j < valeurs.length; j++) ids.push(texteCellule(valeurs[j][0]));
      id = prochainId('RNC', ids);
      ligne[0] = id;
      sh.appendRow(ligne);
    }
    remplacerChoix(id, choix);
    return { id: id, eleveId: eleveId, date: date, enregistreLe: quand };
  });
}

function remplacerChoix(id, choix) {
  var sh = feuille(FEUILLE_CHOIX);
  var valeurs = sh.getDataRange().getValues();
  for (var i = valeurs.length - 1; i >= 1; i--) {
    if (texteCellule(valeurs[i][0]) === id) sh.deleteRow(i + 1);
  }
  if (!choix.length) return;
  var lignes = [];
  for (var c = 0; c < choix.length; c++) {
    lignes.push([id, choix[c].section, choix[c].type, choix[c].code]);
  }
  sh.getRange(sh.getLastRow() + 1, 1, lignes.length, 4).setValues(lignes);
}

function dateValide(texte) {
  var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(texte);
  if (!m) return false;
  var annee = Number(m[1]);
  var mois = Number(m[2]);
  var jour = Number(m[3]);
  var dt = new Date(Date.UTC(annee, mois - 1, jour));
  return dt.getUTCFullYear() === annee && dt.getUTCMonth() === mois - 1 && dt.getUTCDate() === jour;
}

function normaliserChoix(brut, index) {
  var vus = {};
  var exclus = {};
  var out = [];
  var liste = brut || [];
  for (var i = 0; i < liste.length; i++) {
    var c = liste[i] || {};
    var section = String(c.section || '').trim();
    var type = String(c.type || '').trim();
    var code = String(c.code || '').trim();
    if (!section && !type && !code) continue;
    if (type !== 'FORCE' && type !== 'DEFI' && type !== 'STRATEGIE') {
      throw new Error('Choix inconnu.');
    }
    if (!index.titres[section]) throw new Error('Choix inconnu.');
    var cle = section + '|' + type + '|' + code;
    if (vus[cle]) continue;
    if (type === 'FORCE' || type === 'DEFI') {
      if (!index.items[section + '|' + code]) throw new Error('Choix inconnu.');
      var conduite = section + '|' + code;
      if (exclus[conduite] && exclus[conduite] !== type) {
        throw new Error('Une même conduite ne peut pas être à la fois une force et un défi.');
      }
      exclus[conduite] = type;
    } else if (!index.liens[section + '|' + code]) {
      throw new Error('Choix inconnu.');
    }
    vus[cle] = true;
    out.push({ section: section, type: type, code: code });
  }
  return out;
}
