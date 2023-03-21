# Flexport Productivity Infrastructure Take Home

This repository contains a python backend service. This service provides a simple REST api for
playing "Rock, Paper, Scissors" with a computer.


## Running service

### Create virtualenv (optional)

```bash
python -m venv venv
```

### Install dependencies

```bash
python -m pip install -U -r requirements.txt
```

### Running tests

```bash
PYTHONPATH="${PYTHON_PATH}:./src" python -m pytest -v tests/unit
PYTHONPATH="${PYTHON_PATH}:./src" python -m pytest -v tests/functional
```

### Run it

```bash
flask --app src/rock_paper_scissors/app  run
```


## Testing service

```bash
curl http://127.0.0.1:5000/health
```

```bash
curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/rps -d '{"move": "Rock"}'
```
