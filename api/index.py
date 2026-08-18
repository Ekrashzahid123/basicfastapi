from fastapi import Request
from fastapi.responses import JSONResponse
from app.main import app

@app.middleware("http")
async def fix_vercel_path(request: Request, call_next):
    if "debug" in request.query_params:
        return JSONResponse({
            "headers": dict(request.headers),
            "scope_path": request.scope.get("path"),
        })

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
