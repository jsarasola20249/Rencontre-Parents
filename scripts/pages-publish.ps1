# Publica github-pages/ en la rama gh-pages (GitHub Pages, sin Actions).
# Ejecutar: powershell -ExecutionPolicy Bypass -File scripts/pages-publish.ps1

$ErrorActionPreference = "Stop"
$repo = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $repo

$pendiente = git status --porcelain
if ($pendiente) {
  Write-Error "Hay cambios sin commit. Haz commit y push a main antes de publicar la página."
}

git fetch origin

$ramaRemota = git rev-parse --verify "origin/gh-pages" 2>$null
if (-not $ramaRemota) {
  git branch -D gh-pages 2>$null | Out-Null
  git subtree split --prefix=github-pages -b gh-pages
  git push -u origin gh-pages
  Write-Host "Publicada la rama gh-pages."
  exit 0
}

$trabajo = Join-Path $env:TEMP "rencontre-pages-publish"
if (Test-Path $trabajo) {
  git worktree remove $trabajo --force 2>$null | Out-Null
  if (Test-Path $trabajo) { Remove-Item $trabajo -Recurse -Force }
}

git worktree add $trabajo origin/gh-pages
try {
  Copy-Item -Path (Join-Path $repo "github-pages\*") -Destination $trabajo -Recurse -Force
  Set-Location $trabajo
  git add -A
  $cambio = git status --porcelain
  if (-not $cambio) {
    Write-Host "gh-pages ya está al día."
    exit 0
  }
  $nombre = git config user.name
  $correo = git config user.email
  if (-not $nombre -or -not $correo) {
    Write-Error "Git no tiene user.name y user.email. Configúralos y vuelve a ejecutar este script."
  }
  git commit -m "Publicar la página de instalación."
  git push origin HEAD:gh-pages
  Write-Host "gh-pages actualizada."
}
finally {
  Set-Location $repo
  git worktree remove $trabajo --force
}
