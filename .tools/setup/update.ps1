.venv/Scripts/activate
pip install -U pip  # throws [WinError 5], but still works on its own
pip install -U setuptools wheel  # must be done separately from above
pip install -U -r .tools/requirements/requirements_dev.txt
pip uninstall -y propshop
pip install -e .
