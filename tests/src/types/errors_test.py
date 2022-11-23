import pytest

from src.types.errors import ErrorResponse


@pytest.mark.parametrize(
    ("status_code", "payload", "expected_dict"),
    [
        (400, {"foo": "bar"}, {"foo": "bar", "message": "message"}),
        (400, {}, {"message": "message"}),
        (None, None, {"message": "message"}),
    ],
)
def test_can_instantiate_ErrorResponse(status_code, payload, expected_dict):
    message = "message"
    error_response = ErrorResponse(message, status_code, payload)
    assert error_response.message == message
    assert error_response.status_code == status_code
    assert error_response.payload == payload
    assert error_response.to_dict() == expected_dict
