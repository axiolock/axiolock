# Démarrage

## Prérequis

- Python 3.11 ou une version plus récente
- `pip`

## Installation

Depuis PyPI :

```bash
python -m pip install axiolock
```

Pour travailler depuis le dépôt :

```bash
git clone https://github.com/axiolock/axiolock.git
cd axiolock
python -m pip install -e ".[dev]"
```

## Premier contrôle

Vérifiez que le package est importable :

```bash
python -c "import axiolock; print(axiolock.__name__)"
```

Les vérifications du projet sont :

```bash
python -m pytest
python -m ruff check .
python -m build
```

## Développement de la documentation

Installez l'extra de documentation puis lancez le serveur local :

```bash
python -m pip install -e ".[docs]"
python -m mkdocs serve
```

Le site sera disponible à l'adresse `http://127.0.0.1:8000/`.
