# Desplegar Rencontre de parents

Un paso cada vez. El proyecto de Google es nuevo: no reutilices el de fichaje.

Cuando el proyecto ya existe y quieres subir código sin pegar a mano: [CLASP.md](CLASP.md).

## Antes de empezar

- La cuenta de Google del enseignant (la Web App solo se abre con esa cuenta).
- Esta carpeta en el PC.
- Un bloc de notas para tres datos: **URL del Sheet**, **URL de la Web App**, **ID del script**.

## Parte A — Proyecto vacío

1. Entra en [script.google.com](https://script.google.com) con esa cuenta.
2. **Nuevo proyecto**.
3. Renómbralo a `Rencontre de parents`.
4. Engranaje → **Configuración del proyecto**. Copia el **ID del script**.
5. En esa página, marca **Mostrar el archivo de manifiesto appsscript.json**.
6. Pega el ID en `.clasp.json`, en `scriptId`. No es la URL que termina en `/exec`.

## Parte B — Subir el código

En la terminal, en esta carpeta:

```text
powershell -ExecutionPolicy Bypass -File scripts/clasp-push.ps1
```

Eso copia `frontend/index.html` a `backend/index.html` y lo sube con los `.gs`.

Si aún no has hecho `clasp login`, sigue antes [CLASP.md](CLASP.md).

### Pegar a mano, si clasp no está

En Apps Script el nombre no lleva extensión. El HTML tiene que llamarse `index`.

| Archivo en el PC | Nombre en Google |
|------------------|------------------|
| `backend/Code.gs` | `Code` |
| `backend/Setup.gs` | `Setup` |
| `backend/ConfigService.gs` | `ConfigService` |
| `backend/ElevesService.gs` | `ElevesService` |
| `backend/RencontreService.gs` | `RencontreService` |
| `backend/Referentiel.gs` | `Referentiel` |
| `frontend/index.html` | `index` (HTML) |
| `backend/appsscript.json` | `appsscript.json` |

El manifiesto debe quedar con `"access": "MYSELF"` y `"timeZone": "America/Toronto"`.

## Parte C — Sheet y carpeta

1. En el desplegable de funciones, elige **`setupRencontre`**.
2. **Ejecutar**. Autoriza Drive y Sheets.
3. Si Google dice que no ha verificado la app: **Avanzado** → **Ir a Rencontre de parents** → **Permitir**.
4. En el registro tiene que aparecer `Tableur prêt : https://docs.google.com/...` y `Dossier : https://drive.google.com/...`.

En Drive, dentro de **Rencontre de parents**:

- El Sheet **Rencontre de parents**, con las pestañas `Enseignant`, `Élèves`, `Rencontres`, `Choix`, `Grille`, `Stratégies`, `Correspondance`.
- La carpeta **Identité**.

5. En **Identité**, sube el logo del colegio como `logo.png` o `logo.jpg`.

Volver a ejecutar `setupRencontre` no borra alumnos ni rencontres. Sí reescribe las tres pestañas del catálogo.

## Parte D — Publicar

1. **Implementar** → **Nueva implementación**.
2. Tipo: **Aplicación web**.
3. **Ejecutar como:** Yo.
4. **Quién tiene acceso:** Solo yo.
5. **Implementar** y copia la URL que termina en `/exec`.

Ábrela en Chrome, con la misma cuenta. Tienes que ver **Rencontre de parents**, no el HTML en crudo.

Esa URL es la que va en `github-pages/index.html`, en la constante `WEB_APP_URL`.

## Parte E — Prueba

1. Pestaña **Enseignant**. Rellena nom, école, courriel, téléphone, classe, année. **Enregistrer**.
2. El texto bajo el formulario dice si encontró el logo. **Ouvrir le dossier Identité** abre Drive.
3. **Élèves**. Añade un alumno. Tiene que aparecer una fila en la pestaña `Élèves`.
4. **Rencontre**. Elige el alumno y la fecha. Marca una force y el défi de la misma línea: el otro se desmarca. Marca una stratégie. Escribe una note pour la rencontre. **Enregistrer**.
5. En el Sheet: una fila en `Rencontres` y filas en `Choix`. `Enregistré le` lleva fecha y hora.
6. **Imprimer**. En la vista previa de impresión se ven el nombre, el enseignant y lo marcado. No se ve la note. El logo sale si el archivo está en Identité; si no, queda el marco con la palabra Logo.
7. **Suivi**. La rencontre aparece por fecha. **Ouvrir** vuelve a cargarla. **Nouvelle rencontre** crea otra ficha, no pisa la anterior.
8. **Archiver** quita al alumno de las rencontres nuevas. Sigue en Suivi.

## Parte F — Instalarla en el ordenador

Los archivos de `github-pages/` se publican con GitHub Pages (ver el README de esa carpeta).

1. Pega la URL `/exec` en `WEB_APP_URL` de `github-pages/index.html`.
2. Commit, push a `main` y ejecuta `scripts/pages-publish.ps1`. Eso actualiza la rama `gh-pages`, que es la que sirve el sitio.
3. En Chrome, abre `https://jsarasola20249.github.io/Rencontre-Parents/`.
4. Menú del navegador → **Instalar la aplicación** (o el icono de instalar en la barra de direcciones).

El botón **Ouvrir l'application** abre la Web App en la misma pestaña. Úsalo si el recuadro se queda en la pantalla de login de Google: esa pantalla no siempre cabe dentro de un iframe. La sesión tiene que ser la cuenta propietaria.

## Cuando cambies código

1. `scripts/clasp-push.ps1`
2. **Implementar** → **Administrar implementaciones** → lápiz → **Nueva versión** → **Implementar**.

O `scripts/clasp-deploy.ps1` si ya guardaste el ID de implementación en `.clasp-deploy-id` (una línea, el que empieza por `AKfyc`). No crees una implementación nueva: cambiaría la URL.

Si la pantalla no cambia, faltó la versión nueva.

## Si algo falla

| Qué ves | Qué hacer |
|---------|-----------|
| « Exécutez setupRencontre… » | Parte C. |
| « Ouvrez cette page depuis l'application Web » | Estás abriendo el HTML del PC, no la URL `/exec`. |
| Pide login a otra persona | El acceso de la implementación no es **Solo yo**, o la sesión de Chrome es otra cuenta. |
| El iframe no entra | **Ouvrir l'application**. |
| No hay logo | `logo.png` o `logo.jpg` en **Identité**, y recarga. Si pesa más de 2 Mo, usa una imagen más ligera. |
| Falta una pestaña | Vuelve a ejecutar `setupRencontre`. |
