# Officiate.IO.API

## Developer Setup

- Install Poetry [insert link here]
    - Preferably use pipx, and pyenv
- In root directory `poetry install -vv`
- Activate virtual environment [add instructions for poetry venv in project]
    ```bash
    # Linux/Mac
    . .venv\bin\activate

    # Windows
    .venv\Scripts\activate
    ```
- Setup precommit
    ```bash
    python -m pre-commit install
    python -m pre-commit install -t pre-push
    ```
- Optionally run pre-commit `pre-commit run --all-files`
