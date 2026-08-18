from fastapi import FastAPI, Request

from app.routes.students import router as student_router

app = FastAPI(
    title="Student Management API",
    version="1.0.0",
    description="A simple REST API for managing student records using FastAPI.",
)


@app.middleware("http")
async def fix_vercel_path(request: Request, call_next):
    captured_path = request.query_params.get("path")

    if captured_path is not None:
        if not captured_path.startswith("/"):
            captured_path = "/" + captured_path
        request.scope["path"] = captured_path
    elif request.scope["path"].startswith("/api/index"):
        clean_path = request.scope["path"].replace("/api/index", "", 1)
        request.scope["path"] = clean_path if clean_path != "" else "/"

    return await call_next(request)


@app.get("/")
def home():
    return {"message": "Welcome to the Student Management API!"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is healthy and running successfully.",
    }


app.include_router(student_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
