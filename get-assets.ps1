# Downloads every image the site needs into .\assets (Wix originals + Higgsfield generations).
Set-Location $PSScriptRoot; New-Item -ItemType Directory -Force assets | Out-Null
foreach ($f in @("assets-manifest.txt","generated-manifest.txt")) {
  Get-Content $f | ForEach-Object { if ($_ -match "^(.+?)\|(.+)$") { Write-Host "  $($Matches[1])"; Invoke-WebRequest -Uri $Matches[2] -OutFile ("assets\" + $Matches[1]) } }
}
Write-Host "Done."
