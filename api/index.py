from fastapi import Request
from app.main import app

@app.middleware("http")
async def fix_vercel_path(request: Request, call_next):
    # Retrieve the original client requested path from Vercel headers
    forwarded_path = (
        request.headers.get("x-vercel-forwarded-path")
        or request.headers.get("x-forwarded-uri")
        or request.headers.get("x-original-uri")
    )

    if forwarded_path:
        request.scope["path"] = forwarded_path.split("?")[0]
    elif request.scope["path"].startswith("/api/index"):
        clean_path = request.scope["path"].replace("/api/index", "", 1)
        request.scope["path"] = clean_path if clean_path != "" else "/"

    return await call_next(request)
