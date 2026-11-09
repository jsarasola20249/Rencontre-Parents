# GitHub Pages — instalar Rencontre de parents

Estos archivos se publican como sitio (la raíz del sitio, no una subcarpeta de la URL):

https://jsarasola20249.github.io/Rencontre-Parents/

La rama `gh-pages` es la que sirve GitHub Pages. Después de cambiar esta carpeta, hacer commit y push a `main`:

```
powershell -ExecutionPolicy Bypass -File scripts/pages-publish.ps1
```

1. Cuando exista la Web App, pega su URL `/exec` en `index.html`, constante `WEB_APP_URL`.
2. Commit, push a `main`, y el script de arriba.
3. En Chrome: esa dirección → **Instalar**.

El botón **Ouvrir l'application** abre la Web App fuera del iframe. Hace falta la cuenta de Google propietaria del script.

En el repo: Settings → Pages → Deploy from a branch → rama `gh-pages` → carpeta `/ (root)`.
