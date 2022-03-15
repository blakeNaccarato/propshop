copier -f -r 9087cd5
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv
. tooling/update.ps1
