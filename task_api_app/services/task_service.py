import logging
from task_api_app.database.database import get_connection

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def create_task(title, prority):
    conn = None 
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, priority) VALUES (?, ?)', (title, prority))
        conn.commit()
        return {"message": "Task created successfully"}
    
    except Exception as e:
        logging.error(f"create_task error: {e}")
        return None
    finally:
        if conn:
            conn.close()
    
def get_all_tasks():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
     
        
        return [dict(row) for row in rows]
    
        conn.commit()
        return {"message": "Get all tasks successfully"}

    except Exception as e:
        logging.error(f"get_tasks error: {e}")
        return None 
    
    finally:
        if conn:
            conn.close()

def get_task(task_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks WHERE id =?", (task_id,))
        rows = cursor.fetchone()
     
        
        return [dict(row) for row in rows]
    
        conn.commit()
        return {"message": "Task selected successfully"}

    except Exception as e:
        logging.error(f"get_task error: {e}")
        return None 
    
    finally:
        if conn:
            conn.close()

def update_tasks(task_id, title=None, priority=None):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET title = COALESCE(?, title),
                Priority = COALESCE(?, priority)
            WHERE id = ?
        """, (title, priority, task_id))

        conn.commit()
        return {"message": "Task updated successfully"}

    except Exception as e:
        logging.error(f"update_tasks error: {e}")
        return None 
    
    finally:
        if conn:
            conn.close()

def delete_task(task_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?", (task_id)
            )

        conn.commit()
        return {"message": "Task deleted successfully"}

    except Exception as e:
        logging.error(f"delete_task error: {e}")
        return None 
    
    finally:
        if conn:
            conn.close()