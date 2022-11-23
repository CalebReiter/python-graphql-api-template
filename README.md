# Generic API

## Developer Setup

- Install [Poetry](https://python-poetry.org/docs/)
    - Set poetry config `poetry config virtualenvs.in-project true` to have poetry create virtual env inside project.
    - Preferably use pipx, and pyenv
- In root directory `poetry install -vv`
- Activate virtual environment
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
