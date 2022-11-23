"""Nox configuration."""
from typing import List

from nox_poetry import session
from tomlkit import parse

with open("pyproject.toml") as f:
    pyproject = parse(f.read())

SRC_DIR = pyproject["tool"]["poetry"]["packages"][0]["include"]


def get_dependency_group(group: str) -> List[str]:
    """Get dependencies of a given group from the pyproject.toml.

    Args:
        group (str): group to get dependencies for

    Returns:
        List[str]: list of dependencies
    """
    return [
        key
        for key in pyproject["tool"]["poetry"]["group"][group]["dependencies"].keys()
    ]


@session(python=["3.11"])
def tests(session):
    """Run pytest.

    Args:
        session: Nox Session.
    """
    # Pytest command. "python -m pytest -vv --cov={SRC_DIR} --cov-branch --cov-report=html --cov-fail-under=95 tests"
    dependencies = get_dependency_group("test")


@session(python=["3.11"])
def mypy(session):
    """Run mypy.

    Args:
        session: Nox Session.
    """
    dependencies = get_dependency_group("mypy")
    session.install(*dependencies)
    # poetry add lxml required
    # mypy command: mypy --html-report mypy-report --txt-report mypy-report --show-error-codes
    session.run("mypy", "--show-error-codes")


@session(python=["3.11"])
def xenon(session):
    """Run xenon.

    Args:
        session: Nox Session.
    """
    dependencies = get_dependency_group("xenon")
    session.install(*dependencies)
    session.run(
        "xenon",
        "--max-absolute",
        "B",
        "--max-modules",
        "A",
        "--max-average",
        "A",
        SRC_DIR,
    )


@session(python=["3.11"])
def lint(session):
    """Run flakeheaven.

    Args:
        session: Nox Session.
    """
    dependencies = get_dependency_group("lint")
    session.install("flakeheaven")
    session.install(*dependencies)
    # flakeheaven command: flakeheaven lint SRC_DIR tests --format=html --htmldir=flake8-report
    session.run("flakeheaven", "lint", SRC_DIR, "tests")
