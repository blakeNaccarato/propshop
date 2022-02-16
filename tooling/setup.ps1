copier -f -r 679fe01
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv
.venv/Scripts/activate
pip install -U pip  # throws [WinError 5], but works
pip install -U setuptools wheel  # must be done separately from above
pip install -r tooling/requirements_dev.txt
pip uninstall -y propshop
pip install -e .
