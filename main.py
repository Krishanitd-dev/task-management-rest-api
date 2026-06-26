from fastapi import FastAPI
from task_api_app.routes.tasks import router as task_router
from task_api_app.database.database import init_db, get_connection
from task_api_app.config import APP_NAME

app = FastAPI(title=APP_NAME)

init_db()
app.include_router(task_router)

@app.get("/health")
def health():
    try:
        conn = get_connection()
        conn.close()

        return {"status": "ok",
            "database": "connected"}
    except Exception as e:
        return {"status": "Failed",
            "database": str(e)}
            
@app.get("/version")
def version():
    return {"version": "1.0.0"}
