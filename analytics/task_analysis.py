import pandas as pd
import numpy as np


def generate_task_analytics(tasks):

    if not tasks:

        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0
        }

    task_data = []

    for task in tasks:

        task_data.append({
            "status": task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    completed_tasks = len(
        df[df["status"] == "Completed"]
    )

    pending_tasks = len(
        df[df["status"] == "Pending"]
    )

    completion_percentage = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    )

    return {

        "total_tasks": total_tasks,

        "completed_tasks": completed_tasks,

        "pending_tasks": pending_tasks,

        "completion_percentage": completion_percentage
    }