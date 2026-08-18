from fastapi import Request
from app.main import app

@app.middleware("http")
async def fix_vercel_path(request: Request, call_next):
    # Vercel 58+ rewrites path to /api/index. Restore original client path.
    raw_path = request.headers.get("x-matched-path")
    if raw_path:
        request.scope["path"] = raw_path
    elif request.scope["path"].startswith("/api/index"):
        new_path = request.scope["path"].replace("/api/index", "", 1)
        request.scope["path"] = new_path if new_path != "" else "/"

    return await call_next(request)
