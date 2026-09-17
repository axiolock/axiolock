# Getting started

## Prerequisites

- Python 3.11 or newer
- `pip`

## Installation

From PyPI:

```bash
python -m pip install axiolock
```

For local development:

```bash
git clone https://github.com/axiolock/axiolock.git
cd axiolock
python -m pip install -e ".[dev]"
```

## First check

Check that the package can be imported:

```bash
python -c "import axiolock; print(axiolock.__name__)"
```

Run the project checks with:

```bash
python -m pytest
python -m ruff check .
python -m build
```

## Documentation development

Install the documentation extra and start the local server:

```bash
python -m pip install -e ".[docs]"
python -m mkdocs serve
```

The site will be available at `http://127.0.0.1:8000/`.
