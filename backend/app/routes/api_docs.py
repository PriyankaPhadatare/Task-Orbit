from pathlib import Path

from flask import Blueprint, send_from_directory

bp = Blueprint("api_docs", __name__, url_prefix="/api")
STATIC_DIR = Path(__file__).resolve().parents[1] / "static"


@bp.get("/docs")
def docs():
    return send_from_directory(STATIC_DIR, "api-docs.html")


@bp.get("/openapi.json")
def openapi_spec():
    return send_from_directory(STATIC_DIR, "openapi.json")