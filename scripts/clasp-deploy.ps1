# Nueva versión de la Web App EXISTENTE (misma URL).
# Sin .clasp-deploy-id no crea un deploy nuevo.

$ErrorActionPreference = "Stop"
$repo = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $repo

$idFile = Join-Path $repo ".clasp-deploy-id"
if (-not (Test-Path $idFile)) {
  Write-Host "Falta .clasp-deploy-id. Estas son las implementaciones:"
  npx.cmd --yes "@google/clasp" list-deployments
  Write-Host ""
  Write-Host "Copia el ID de la Aplicacion web a .clasp-deploy-id (una sola linea)."
  Write-Host "Luego vuelve a ejecutar este script. NO uses clasp deploy: crearia otra URL."
  exit 1
}

$deployId = (Get-Content $idFile -Raw).Trim()
npx.cmd --yes "@google/clasp" redeploy $deployId
