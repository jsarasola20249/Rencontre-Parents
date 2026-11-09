# Plan — Rencontre de parents

Orden en el que está construida esta versión. El detalle de datos y pantallas está en [SPEC.md](SPEC.md).

## 1. Documentos

`SPEC.md`, este plan, `CHANGELOG.md`, `README.md`, `DEPLOY.md` y `CLASP.md`.

## 2. Catálogo

Pasar la grille y el repertorio de stratégies a JSON, con la correspondance de [SPEC.md](SPEC.md). `scripts/build-referentiel.py` genera también `backend/Referentiel.gs`, que es la copia que lee Apps Script.

## 3. Backend

`setupRencontre` crea el Sheet y la carpeta `Identité`. Los servicios guardan alumnos, la ficha del enseignant, el logo y las rencontres con fecha y hora. El catálogo se vuelve a escribir en las pestañas de lectura cada vez que se ejecuta el setup; las filas de alumnos y rencontres no se borran.

## 4. Pantalla

Una sola `frontend/index.html`, en francés: Élèves, Rencontre, Suivi, Enseignant. En cada sección, tres listas de casillas (forces, défis, stratégies), no un solo valor.

## 5. Impresión

Hoja para las familias con el marco del logo, los datos del enseignant y solo lo marcado. Las notes pour la rencontre se quedan en el Sheet.

## 6. Instalación en el ordenador

Mismo esquema que fichaje: GitHub Pages con iframe, `manifest.webmanifest` y service worker.

Como el acceso es solo el propietario, el login de Google a veces no cabe en el iframe. La página muestra siempre el botón **Ouvrir l'application**, que abre la Web App en la misma pestaña.

La URL `/exec` se pega en `github-pages/index.html` cuando exista el deploy. Hasta entonces la página lo dice en francés y no carga un iframe vacío.

## Después de esta versión

No entra aquí: varias clases, acceso de las familias, PDF guardado en Drive, ni cambiar los textos del catálogo desde la app.
