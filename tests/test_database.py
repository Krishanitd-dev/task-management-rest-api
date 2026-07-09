from task_api_app.services.task_service import create_task

def test_create_task():
    result = create_task(  "Testing 1", 1)
    assert result["message"] == "Task created successfully"


