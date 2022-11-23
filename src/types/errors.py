"""Error Types."""

from typing import Any, Dict, Optional


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
