import pytest
from flask.testing import FlaskClient

from src.router import app


@pytest.fixture()
def client() -> FlaskClient:
    """Configure test client.

    Returns:
        FlaskClient: The Test Client
    """
    return app.test_client()
