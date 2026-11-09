/**
 * ElevesService.gs — Alta, cambio de nombre y archivo de alumnos.
 */

function listerEleves() {
  var lignes = lireDonnees(FEUILLE_ELEVES);
  var eleves = [];
  for (var i = 0; i < lignes.length; i++) {
    var ligne = lignes[i];
    eleves.push({
      id: texteCellule(ligne[0]),
      prenom: texteCellule(ligne[1]),
      nom: texteCellule(ligne[2]),
      actif: texteCellule(ligne[3]) === 'NON' ? 'NON' : 'OUI',
      creeLe: horodatageCellule(ligne[4])
    });
  }
  eleves.sort(function (a, b) {
    if (a.actif !== b.actif) return a.actif === 'OUI' ? -1 : 1;
    var na = (a.nom + ' ' + a.prenom).toLowerCase();
    var nb = (b.nom + ' ' + b.prenom).toLowerCase();
    if (na < nb) return -1;
    if (na > nb) return 1;
    return a.id < b.id ? -1 : 1;
  });
  return eleves;
}

function trouverEleve(id) {
  var eleves = listerEleves();
  for (var i = 0; i < eleves.length; i++) {
    if (eleves[i].id === id) return eleves[i];
  }
  return null;
}

function enregistrerEleve(data) {
  return avecVerrou(function () {
    data = data || {};
    var prenom = String(data.prenom || '').trim();
    var nom = String(data.nom || '').trim();
    if (!prenom || !nom) {
      throw new Error('Indiquez le prénom et le nom.');
    }
    var sh = feuille(FEUILLE_ELEVES);
    var valeurs = sh.getDataRange().getValues();
    var id = String(data.id || '').trim();
    if (id) {
      for (var i = 1; i < valeurs.length; i++) {
        if (texteCellule(valeurs[i][0]) === id) {
          sh.getRange(i + 1, 2, 1, 2).setValues([[prenom, nom]]);
          return {
            id: id,
            prenom: prenom,
            nom: nom,
            actif: texteCellule(valeurs[i][3]) === 'NON' ? 'NON' : 'OUI',
            creeLe: horodatageCellule(valeurs[i][4])
          };
        }
      }
      throw new Error('Cet élève est introuvable.');
    }
    var ids = [];
    for (var j = 1; j < valeurs.length; j++) ids.push(texteCellule(valeurs[j][0]));
    var nouveau = prochainId('ELV', ids);
    var cree = maintenantTexte();
    sh.appendRow([nouveau, prenom, nom, 'OUI', cree]);
    return { id: nouveau, prenom: prenom, nom: nom, actif: 'OUI', creeLe: cree };
  });
}

function definirActif(data) {
  return avecVerrou(function () {
    data = data || {};
    var id = String(data.id || '').trim();
    var actif = data.actif === 'NON' ? 'NON' : 'OUI';
    var sh = feuille(FEUILLE_ELEVES);
    var valeurs = sh.getDataRange().getValues();
    for (var i = 1; i < valeurs.length; i++) {
      if (texteCellule(valeurs[i][0]) === id) {
        sh.getRange(i + 1, 4).setValue(actif);
        return {
          id: id,
          prenom: texteCellule(valeurs[i][1]),
          nom: texteCellule(valeurs[i][2]),
          actif: actif,
          creeLe: horodatageCellule(valeurs[i][4])
        };
      }
    }
    throw new Error('Cet élève est introuvable.');
  });
}
