$GLOBAL_PYTHON = 'py -3.10'
try { Invoke-Expression $("$GLOBAL_PYTHON --version") } catch [System.Management.Automation.CommandNotFoundException] { $GLOBAL_PYTHON = 'python3.10' }
Remove-Item -ErrorAction SilentlyContinue -Recurse -Force .venv
Invoke-Expression "$GLOBAL_PYTHON -m venv .venv --upgrade-deps"
. ./update.ps1
pre-commit install --install-hooks
