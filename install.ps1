Write-Host "Running $env:PROJECT_DIR\install.ps1..."  -ForegroundColor Yellow
if (Test-Path -Path "$env:PROJECT_DIR\pyproject.toml")
    {poetry install}
