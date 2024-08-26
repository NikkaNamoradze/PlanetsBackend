from fastapi import APIRouter

entry_root = APIRouter()


@entry_root.get("/")
def api_running():
    res = {
        "status": "ok",
        "message": "Api is running"
    }
    return res
