copier -f -r c883f43
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv --upgrade-deps
. .tooling/update.ps1
