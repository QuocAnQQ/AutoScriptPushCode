param(
  [string]$Branch = "main",
  [string]$RepoDir = "C:\GitPushAutomation\runner\myapp",
  [string]$Entry = "python main.py"  # đổi nếu bạn dùng Node/.NET/Maven/Docker
)
$ErrorActionPreference = "Stop"
Set-Location -Path $RepoDir

# 1) Kiểm tra commit mới
git fetch origin $Branch | Out-Null
$local  = (git rev-parse HEAD).Trim()
$remote = (git rev-parse "origin/$Branch").Trim()
if ($local -eq $remote) {
  Write-Host "[auto_pull_run] No update."
  exit 0
}
Write-Host "[auto_pull_run] New commit detected. Pulling..."

# 2) Pull an toàn
git reset --hard
git clean -fd
git checkout $Branch
git pull --rebase origin $Branch

# 3) (Tuỳ) cài dependency
if (Test-Path "$RepoDir\requirements.txt") { pip install -r requirements.txt }
if (Test-Path "$RepoDir\package.json") { npm ci }

# 4) Chạy app/tests
Write-Host "[auto_pull_run] Running: $Entry"
cmd /c $Entry
Write-Host "[auto_pull_run] Done."
