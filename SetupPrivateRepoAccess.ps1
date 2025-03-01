Write-Host ''

function Remove-RepositoryConfiguration {
    param (
        [Object]$RepoDetails
    )
    Write-Host "Remove configuration" -ForegroundColor Magenta
    poetry config ("http-basic." + $RepoDetails.name) --unset
    poetry source remove $RepoDetails.name
    poetry remove $RepoDetails.name
}

function Publish-RepositoryConfiguration
{
    param (
        [Object]$RepoDetails
    )
    Write-Host "Add configuration" -ForegroundColor Magenta
    poetry source add --priority=supplemental $RepoDetails.name ("https://github.com/" + $RepoDetails.org + "/" + $RepoDetails.name + ".git")
    poetry config ("http-basic." + $RepoDetails.name) ($RepoDetails.user) ($RepoDetails.pwd)
    poetry add --source $RepoDetails.name ("git+https://github.com/" + $RepoDetails.org + "/" + $RepoDetails.name + ".git" + $RepoDetails.version_branch)
}

Write-Host ''
$dateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Host "=[ START $dateTime ]=========================[ SetupPrivateRepo.ps1 ]=" -ForegroundColor Blue
Write-Host "Executing $PSCommandPath..." -ForegroundColor Yellow

$RepoDetails = [PSCustomObject]@{
    name = "PoetryPrivate"
    user = "__token__"
    pwd = $env:GH_REPO_ACCESS_CURR_USER
    org = "BrightEdgeeServices"
    version_branch = "#master"
}
Remove-RepositoryConfiguration -RepoDetails $RepoDetails
#Publish-RepositoryConfiguration -RepoDetails $RepoDetails

Write-Host '-[ END SetupPrivateRepo.ps1 ]---------------------------------------------------' -ForegroundColor Cyan
Write-Host ''
