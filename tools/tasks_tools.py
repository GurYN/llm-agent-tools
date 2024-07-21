def get_tasks() -> list:
    """Get a list of active tasks user have to do. This function will return work to do for the user."""
    return [
        {
            "title": "Task 1",
            "status": "active"
        }
    ]

def create_task(title: str) -> dict:
    """Create a new task or reminder."""
    return {
        "title": title,
        "status": "active"
    }

def complete_task(text: str) -> dict:
    """Mark a task or reminder as completed."""
    return {
        "title": text,
        "status": "completed"
    }
