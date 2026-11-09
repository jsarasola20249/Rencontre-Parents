# Especificación — Rencontre de parents

App de un solo enseignant de 1re année. La pantalla, el Google Sheet, las carpetas de Drive y la hoja impresa están en francés. Los comentarios del código están en español.

**Acceso:** la Web App se ejecuta como el propietario y solo esa cuenta de Google puede abrirla.

**Tiempo:** cada rencontre es una ficha con la fecha que elige el enseignant (por defecto, hoy en `America/Toronto`) y la hora del último guardado. No hay tope de tres. Reabrir una ficha la actualiza; « Nouvelle rencontre » crea otra.

## Pantallas

| Zona | Qué hace |
|------|----------|
| Élèves | Alta, cambio de nombre y archivo. Un alumno archivado sigue en Suivi. |
| Rencontre | Elige alumno y fecha. En cada sección marca varias forces, varios défis y varias stratégies. Una misma conducta no puede ser force y défi a la vez. |
| Suivi | Lista las rencontres del alumno, de la más reciente a la más antigua. Ouvrir o Imprimer. |
| Enseignant | Prénom, nom, courriel, téléphone, école, classe, année scolaire. El logo no se sube aquí: se lee de Drive. |

La síntesis (forces principales, défis prioritaires, objectif, commentaires, notes pour la rencontre) es texto libre. Las notes no se imprimen.

## Impresión

`window.print()` de la ficha que está en pantalla, no un PDF en Drive.

Sale: logo (o un marco con la palabra Logo), école, nom del enseignant, classe, année, courriel, téléphone, nom del alumno, fecha, y solo las secciones con algo marcado. Cada stratégie lleva el nombre, « Comment l’utiliser » y el ejemplo. Después, la síntesis si hay texto.

No salen las notes internes ni los identificadores.

## Catálogo

Origen: `scripts/build-referentiel.py`. Al ejecutarlo reescribe `referentiel/` y `backend/Referentiel.gs`.

- `referentiel/grille.json` — 9 secciones, 126 conductas. El código (`COMP-01`) guarda la pareja force (presente) / défi (infinitivo).
- `referentiel/strategies.json` — 69 stratégies, con bloque, uso y ejemplo.
- `referentiel/correspondance.json` — qué stratégies aparecen en cada sección.

Cada sección muestra su bloque y, además, las stratégies transversales.

| Sección | Bloque propio |
|---------|----------------|
| Comportement et relations avec les autres | Comportement et autorégulation |
| Motivation, participation et persévérance | Motivation et engagement dans les apprentissages |
| Attention et concentration | Attention et concentration |
| Autonomie et organisation | Fonctions exécutives et autonomie |
| Français – Lecture | Sonidos, syllabes, relecture y compréhension del bloque de français |
| Français – Écriture | Phrase, mots, écriture y relecture de ese bloque |
| Mathématiques – Numération | Representación, suite, comparaison, décomposition |
| Mathématiques – Calcul et résolution de problèmes | Manipulation, calcul oral, problème du quotidien, vérification |
| Motricité fine et réalisation des travaux | Lista corta: matériel, rutinas, espacio de trabajo, découper la tâche. No hay capítulo propio en el repertorio. |

« Revoir les notions à différents moments » está en numération y en calcul. La síntesis no tiene desplegables.

El enseignant no edita el catálogo. `setupRencontre` lo copia a las pestañas `Grille`, `Stratégies` y `Correspondance` (aviso de solo lectura).

## Drive

`setupRencontre()` crea, una vez:

- Carpeta `Rencontre de parents` / subcarpeta `Identité`
- Sheet `Rencontre de parents` dentro de esa carpeta

Logo: el primer archivo de `Identité` que se llame `logo.png`, `logo.jpg`, `logo.jpeg` o `logo.webp` (sin distinguir mayúsculas). Máximo 2 Mo.

### Pestaña Enseignant

Una fila de datos (fila 2).

`Prénom`, `Nom`, `Courriel`, `Téléphone`, `École`, `Classe`, `Année scolaire`

### Pestaña Élèves

`ID` (`ELV-001`), `Prénom`, `Nom`, `Actif` (`OUI` / `NON`), `Créé le`

### Pestaña Rencontres

`ID` (`RNC-001`), `ID élève`, `Date de la rencontre`, `Enregistré le`, `Forces principales`, `Défis prioritaires`, `Objectif`, `Commentaires`, `Notes internes`

### Pestaña Choix

Una fila por casilla marcada: `ID rencontre`, `Section` (código, p. ej. `COMP`), `Type` (`FORCE`, `DEFI` o `STRATEGIE`), `Code`

## Código

| Archivo | Rol |
|---------|-----|
| `backend/Code.gs` | `doGet`, contexto, fechas, catálogo unido |
| `backend/Setup.gs` | `setupRencontre` |
| `backend/ConfigService.gs` | Ficha y logo |
| `backend/ElevesService.gs` | Alumnos |
| `backend/RencontreService.gs` | Rencontres y validación |
| `backend/Referentiel.gs` | Datos del catálogo (generado) |
| `frontend/index.html` | Pantalla. `scripts/clasp-push.ps1` la copia a `backend/index.html` |

`appsscript.json`: zona `America/Toronto`, ejecutar como el propietario, acceso `MYSELF`. El HTML permite iframe (`ALLOWALL`) para la página instalable.

## Aperçu local

Solo para revisar la pantalla en este PC, sin Google:

```text
python -m http.server 8765
```

Abrir `http://127.0.0.1:8765/frontend/index.html?apercu=1`. Los datos se quedan en el navegador.

## Fuera de esta versión

Varias clases en el mismo Sheet, portal para las familias, PDF archivado en Drive, y edición del catálogo desde la app.
