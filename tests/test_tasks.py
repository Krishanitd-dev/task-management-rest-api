def create_task():
    return {
        "message": "Task_1 created successfully",
        "id": 1
    }


def test_create_task():

    result = create_task()

    assert result["message"] == "Task_1 created successfully"