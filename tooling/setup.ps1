copier -f -r 7912c56
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv --upgrade-deps
. tooling/update.ps1
