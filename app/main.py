from fastapi import FastAPI

from app.routes.students import router as student_router

app = FastAPI(
    title="Student Management API",
    version="1.0.0",
    description="A simple REST API for managing student records using FastAPI.",
)


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
