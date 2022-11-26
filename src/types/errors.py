"""Error Types."""

import re
from typing import Any, Dict, List, Optional


class ErrorResponse(Exception):
    """Error for responses."""

    def __init__(
        self,
        message: str,
        status_code: int = 400,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize ErrorResponse.

        Args:
            message (str): error message
            status_code (int): status code for response
            payload (Optional[Dict[str, Any]]): additional payload for error
        """
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary.

        Returns:
            Dict[str, Any]: error as dictionary
        """
        return {**dict(self.payload or {}), "message": self.message}


class ErrorMessages:
    """Contain error messages."""

    @classmethod
    def escaped_message(cls, message: str, *args: List[Any]) -> str:  # pragma: no cover
        """Get error message and escape it.
        
        Args:
            message (str): error message to get
            args (List[Any]): arguments to pass to error message if it is callable
        
        Returns:
            str: escaped error message
        """
        error_message = getattr(cls, message)
        if callable(error_message):
            error_message = error_message(*args)
        return re.escape(error_message)


class FlaskErrorMessages(ErrorMessages):
    """Contain error messages for Flask."""

    NOT_FOUND = "NOT FOUND"

