# Rencontre de parents

Ficha de rencontres de parents para un enseignant de 1re année du primaire (Québec).

El enseignant anota a sus alumnos, guarda una evaluación por fecha (forces, défis y stratégies para la familia) y la imprime el día de la reunión. Los datos viven en un Google Sheet de su Drive. La pantalla, el Sheet, las carpetas y la hoja impresa están en francés.

## Estructura

```
├── SPEC.md              Qué hace y cómo se guardan los datos
├── PLAN.md              Orden de construcción
├── CHANGELOG.md
├── DEPLOY.md            Publicar la Web App
├── CLASP.md             Subir código desde Cursor
├── referentiel/         Grille, stratégies y correspondance (JSON)
├── backend/             .gs y appsscript.json → proyecto GAS
├── frontend/index.html  Pantalla (origen). clasp la copia a backend/
├── github-pages/        Iframe + manifest para instalarla en el ordenador
└── scripts/             clasp y regeneración del catálogo
```

## Fuera de esta versión

- Varias clases en el mismo Sheet
- Portal para las familias
- PDF guardado en Drive
- Editar el catálogo desde la app

Empieza por [DEPLOY.md](DEPLOY.md). El detalle de pantallas y columnas está en [SPEC.md](SPEC.md).
