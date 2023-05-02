from fastapi import FastAPI

from routes import general


def setup_routes(app: FastAPI):
    """
    Each Router specified in routes/* must be referenced in setup_routes(),
    as a new app.include_router() call.
    """
    app.include_router(general.router, prefix="/api", tags=["core"])


TAGS_METADATA = [
    {"name": "core", "description": "General system endpoints for the API."}
]