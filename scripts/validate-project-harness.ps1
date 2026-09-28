[CmdletBinding()]
param(
    [string]$ProjectRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path -LiteralPath $ProjectRoot).Path

$required = @(
    "AGENTS.md",
    "PROJECT_CONTEXT.md",
    "WORKSPACE_MAP.md",
    "COORDINATION.md",
    "QUALITY_GATES.md",
    "harness-config.yaml"
)

$missing = @($required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $root $_) -PathType Leaf) })
if ($missing.Count -gt 0) {
    Write-Error ("HARNESS_STATUS=fail; missing=" + ($missing -join ","))
    exit 1
}

$empty = @($required | Where-Object {
    $path = Join-Path $root $_
    ((Get-Item -LiteralPath $path).Length -eq 0)
})
if ($empty.Count -gt 0) {
    Write-Error ("HARNESS_STATUS=fail; empty=" + ($empty -join ","))
    exit 1
}

$coordination = Get-Content -LiteralPath (Join-Path $root "COORDINATION.md") -Raw
foreach ($marker in @("owner", "acceptance", "stop", "conflict")) {
    if ($coordination -notmatch $marker) {
        Write-Error ("HARNESS_STATUS=fail; COORDINATION.md lacks marker: " + $marker)
        exit 1
    }
}

Write-Output "HARNESS_STATUS=ok"
Write-Output ("PROJECT_ROOT=" + $root)
Write-Output ("REQUIRED_FILES=" + $required.Count)
