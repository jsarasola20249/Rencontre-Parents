# Conectar Cursor y Apps Script

No hace falta dar contraseñas. Google abre el navegador; el push se lanza cuando aceptas el comando.

En este Windows:

- No uses `npx` a secas en PowerShell. Usa **`npx.cmd`**.
- El paquete va entre comillas: `"@google/clasp"`.
- Para abrir el editor: **`open-script`**, no `open`.

La terminal tiene que estar en esta carpeta:

```text
cd "C:\Users\4547\Documents\Cursor\Rencontre des Parents"
```

## Una vez en este PC

### Node.js

```text
node -v
```

Tiene que salir un número (v18 o más). Si falla, instala la LTS en [nodejs.org](https://nodejs.org) y reabre Cursor.

### Login de Google

Con la cuenta dueña del script:

```text
npx.cmd -y "@google/clasp" login
```

Se abre Chrome. **Permitir**. El token queda en tu usuario de Windows. No lo subas a GitHub.

### API de Apps Script

Abre [script.google.com/home/usersettings](https://script.google.com/home/usersettings) y activa la API de Apps Script.

### Script ID

Engranaje del proyecto → **ID del script**. Pégalo en `.clasp.json`.

| Qué | ¿Vale para `.clasp.json`? |
|-----|---------------------------|
| ID del script (engranaje) | Sí |
| ID de implementación `AKfyc…` | No. Va en `.clasp-deploy-id` |
| URL `…/exec` | No. Va en `github-pages/index.html` |

Comprobar:

```text
npx.cmd -y "@google/clasp" open-script
```

Tiene que abrir el proyecto `Rencontre de parents`.

## Subir

```text
powershell -ExecutionPolicy Bypass -File scripts/clasp-push.ps1
```

El script copia `frontend/index.html` sobre `backend/index.html` y hace el push. `backend/index.html` no se guarda en git.

Si Google pregunta si sobrescribe, confirma.

## Nueva versión, misma URL

1. **Implementar → Administrar implementaciones**.
2. Copia el ID de la aplicación web (`AKfyc…`).
3. Créalo en `.clasp-deploy-id` (modelo: `.clasp-deploy-id.example`), una sola línea.
4. Ejecuta:

```text
powershell -ExecutionPolicy Bypass -File scripts/clasp-deploy.ps1
```

Ese archivo está en `.gitignore`. No lo subas.

## Catálogo

Si cambias un texto de la grille o de una stratégie, edita `scripts/build-referentiel.py` y ejecuta:

```text
python scripts/build-referentiel.py
```

Luego vuelve a hacer el push. `Referentiel.gs` no se edita a mano.

## Si algo falla

| Mensaje | Qué hacer |
|---------|-----------|
| `npx.ps1 cannot be loaded` | Usa `npx.cmd`. |
| `Unknown command "clasp open"` | `open-script`, con el paquete entre comillas. |
| `REEMPLAZAR_CON_SCRIPT_ID` | Pega el ID del engranaje. |
| `User has not enabled the Apps Script API` | Actívala en la configuración de usuario de script.google.com. |
| `Unlogged` / 401 | Vuelve a hacer login. |
| Los archivos aparecen dentro de una carpeta `backend` en Google | El push tiene que usar `rootDir`: `backend` (ya está en `.clasp.json`). |
| La pantalla no cambia | Falta una **nueva versión**, no una implementación nueva. |
