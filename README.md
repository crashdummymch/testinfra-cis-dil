# testinfra-cis-dil
Testinfra CIS Distribution Independent Linux Benchmark

## Installation
```
python -m venv venv
source venv/bin/activate
pip install -r requirements_install.txt
```
Create a python virtual environment.
Activate and install requirements.
Now ready to run tests.
## Pytest Run
```
pytest -vs
```

## Pytest Markers

## testinfra-cis-dil variables
### cis-dil/defaults/main.yml
Contains a yaml list of all default values.
Fixture to return default values cis-dil/conftest.py
### overrides/main.ym
Contains a yaml list of override values
Fixture to return overrides conftest.py
