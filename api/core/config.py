import os
from typing import Optional

import pydantic

ENV_FILE = os.getenv("ENV_FILE", ".env")


class BaseSettings(pydantic.BaseSettings):
    """Base class for loading settings.
    The setting variables are loaded from environment settings first, then from the defined env_file.

    Different groups/contexts of settings are created using different classes, that can define an env_prefix which
    will be concatenated to the start of the variable name."""

    class Config:
        env_file = ENV_FILE


class ChatApiSettings(BaseSettings):
    debug: bool = False
    """Whether the app should run in debug mode"""

    host: str = "0.0.0.0"
    """Host where the API is run"""

    port: int = 8080
    """Port at which the API is run"""

    title: str = "Chat API"
    """Title of the API"""

    description: Optional[str] = None
    """Description of the API"""

    version: str = "0.0.1"
    """Version of the API"""

    secret: str = "586e792e5af7d30d90801fbf829e8263"
    """
    App secret used for session, jwt, encryption

    Generate using: node -e "console.log(require('crypto').randomBytes(16).toString('hex'))"
    """

    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/chatappdb"
    )
    """Postgres database URL"""


config = ChatApiSettings()