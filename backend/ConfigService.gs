/**
 * ConfigService.gs — Ficha del enseignant y logo en Drive.
 */

var NOMS_LOGO = ['logo.png', 'logo.jpg', 'logo.jpeg', 'logo.webp'];
var MIME_LOGO = {
  'logo.png': 'image/png',
  'logo.jpg': 'image/jpeg',
  'logo.jpeg': 'image/jpeg',
  'logo.webp': 'image/webp'
};
var TAILLE_LOGO_MAX = 2000000;

function obtenirEnseignant() {
  var sh = feuille(FEUILLE_ENSEIGNANT);
  if (sh.getLastRow() < 2) return enseignantVide();
  var ligne = sh.getRange(2, 1, 1, ENCABEZADOS_ENSEIGNANT.length).getValues()[0];
  return {
    prenom: texteCellule(ligne[0]),
    nom: texteCellule(ligne[1]),
    courriel: texteCellule(ligne[2]),
    telephone: texteCellule(ligne[3]),
    ecole: texteCellule(ligne[4]),
    classe: texteCellule(ligne[5]),
    annee: texteCellule(ligne[6])
  };
}

function enseignantVide() {
  return {
    prenom: '',
    nom: '',
    courriel: '',
    telephone: '',
    ecole: '',
    classe: '',
    annee: ''
  };
}

function enregistrerEnseignant(data) {
  return avecVerrou(function () {
    data = data || {};
    var sh = feuille(FEUILLE_ENSEIGNANT);
    sh.getRange(2, 1, 1, ENCABEZADOS_ENSEIGNANT.length).setValues([[
      String(data.prenom || '').trim(),
      String(data.nom || '').trim(),
      String(data.courriel || '').trim(),
      String(data.telephone || '').trim(),
      String(data.ecole || '').trim(),
      String(data.classe || '').trim(),
      String(data.annee || '').trim()
    ]]);
    return obtenirEnseignant();
  });
}

function obtenirDossier() {
  var id = proprietes().getProperty(PROP_IDENTITE_ID);
  if (!id) {
    throw new Error('Exécutez setupRencontre dans l’éditeur Apps Script.');
  }
  try {
    var dossier = DriveApp.getFolderById(id);
    return {
      nom: NOM_DOSSIER,
      identite: NOM_IDENTITE,
      url: dossier.getUrl()
    };
  } catch (e) {
    throw new Error('Le dossier Identité est introuvable. Exécutez setupRencontre.');
  }
}

function obtenirLogo() {
  var id = proprietes().getProperty(PROP_IDENTITE_ID);
  if (!id) {
    return {
      present: false,
      message: 'Exécutez setupRencontre dans l’éditeur Apps Script.'
    };
  }
  var dossier;
  try {
    dossier = DriveApp.getFolderById(id);
  } catch (e2) {
    return { present: false, message: 'Le dossier Identité est introuvable.' };
  }
  var trouve = chercherLogo(dossier);
  if (!trouve) {
    return {
      present: false,
      message: 'Ajoutez logo.png ou logo.jpg dans le dossier Identité.'
    };
  }
  if (trouve.fichier.getSize() > TAILLE_LOGO_MAX) {
    return {
      present: false,
      message: 'Le logo dépasse 2 Mo. Utilisez une image plus légère.'
    };
  }
  var blob = trouve.fichier.getBlob();
  return {
    present: true,
    mime: MIME_LOGO[trouve.nom] || blob.getContentType() || 'image/png',
    base64: Utilities.base64Encode(blob.getBytes()),
    message: 'Logo trouvé dans le dossier Identité.'
  };
}

function chercherLogo(dossier) {
  var voulu = {};
  for (var i = 0; i < NOMS_LOGO.length; i++) voulu[NOMS_LOGO[i]] = true;
  var fichiers = dossier.getFiles();
  var mejor = null;
  var rangoMejor = NOMS_LOGO.length;
  while (fichiers.hasNext()) {
    var fichier = fichiers.next();
    var nom = fichier.getName().toLowerCase();
    if (!voulu[nom]) continue;
    var rango = NOMS_LOGO.indexOf(nom);
    if (rango !== -1 && rango < rangoMejor) {
      mejor = { fichier: fichier, nom: nom };
      rangoMejor = rango;
    }
  }
  return mejor;
}
