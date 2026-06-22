from fastapi import FastAPI
from task_api_app.routes.tasks import router as task_router
from task_api_app.database.database import init_db
from task_api_app.config import APP_NAME

app = FastAPI(title=APP_NAME)

init_db()
app.include_router(task_router)

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/version")
def version():
    return {"version": "1.0.0"}
