# Copia el HTML a backend/ y sube el proyecto a Apps Script.
# Ejecutar: powershell -ExecutionPolicy Bypass -File scripts/clasp-push.ps1

$ErrorActionPreference = "Stop"
$repo = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $repo

$clasp = Get-Content ".\.clasp.json" -Raw | ConvertFrom-Json
if ($clasp.scriptId -eq "REEMPLAZAR_CON_SCRIPT_ID") {
  Write-Error "Abre .clasp.json y pega el Script ID (engranaje en Apps Script). No es el ID de implementacion ni la URL /exec."
}

Copy-Item ".\frontend\index.html" ".\backend\index.html" -Force
Write-Host "HTML copiado a backend/index.html"
npx.cmd --yes "@google/clasp" push
