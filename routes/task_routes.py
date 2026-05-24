import csv

from io import StringIO

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import jsonify
from flask import make_response

from flask_login import login_required
from flask_login import current_user

from models.task_model import Task
from models.task_model import TaskHistory

from models.extensions import db
from models.extensions import socketio

from analytics.task_analysis import generate_task_analytics


task = Blueprint("task", __name__)


# DASHBOARD

@task.route("/dashboard")

@login_required

def dashboard():

    search = request.args.get("search", "")

    priority = request.args.get("priority", "")

    status = request.args.get("status", "")

    query = Task.query.filter_by(
        user_id=current_user.id,
        deleted=False
    )

    # SEARCH

    if search:

        query = query.filter(
            Task.title.ilike(f"%{search}%")
        )

    # PRIORITY FILTER

    if priority:

        query = query.filter_by(
            priority=priority
        )

    # STATUS FILTER

    if status:

        query = query.filter_by(
            status=status
        )

    tasks = query.order_by(
        Task.created_date.desc()
    ).all()

    analytics = generate_task_analytics(tasks)

    history = TaskHistory.query.filter_by(
        user_id=current_user.id
    ).order_by(
        TaskHistory.timestamp.desc()
    ).all()

    return render_template(
        "dashboard.html",
        tasks=tasks,
        analytics=analytics,
        history=history
    )


# ADD TASK

@task.route("/add-task", methods=["POST"])

@login_required

def add_task():

    title = request.form.get("title")

    description = request.form.get("description")

    priority = request.form.get("priority")

    deadline = request.form.get("deadline")

    new_task = Task(

        title=title,

        description=description,

        priority=priority,

        deadline=deadline,

        status="Pending",

        user_id=current_user.id
    )

    db.session.add(new_task)

    # HISTORY

    history = TaskHistory(

        task_title=title,

        action="Task Added",

        user_id=current_user.id
    )

    db.session.add(history)

    db.session.commit()

    socketio.emit(

        "notification",

        {
            "message": f"Task Added: {title}"
        }
    )

    flash(
        "Task Added Successfully",
        "success"
    )

    return redirect("/dashboard")


# UPDATE STATUS

@task.route("/update-task/<int:id>")

@login_required

def update_task(id):

    task = Task.query.get_or_404(id)

    if task.user_id == current_user.id:

        if task.status == "Pending":

            task.status = "Completed"

            action_text = "Task Completed"

        else:

            task.status = "Pending"

            action_text = "Task Reopened"

        history = TaskHistory(

            task_title=task.title,

            action=action_text,

            user_id=current_user.id
        )

        db.session.add(history)

        db.session.commit()

        socketio.emit(

            "notification",

            {
                "message": action_text
            }
        )

        flash(
            action_text,
            "info"
        )

    return redirect("/dashboard")


# EDIT TASK

@task.route("/edit-task/<int:id>", methods=["GET", "POST"])

@login_required

def edit_task(id):

    task = Task.query.get_or_404(id)

    if task.user_id != current_user.id:

        flash(
            "Unauthorized Access",
            "danger"
        )

        return redirect("/dashboard")

    if request.method == "POST":

        task.title = request.form.get("title")

        task.description = request.form.get(
            "description"
        )

        task.priority = request.form.get(
            "priority"
        )

        task.deadline = request.form.get(
            "deadline"
        )

        task.status = request.form.get(
            "status"
        )

        history = TaskHistory(

            task_title=task.title,

            action="Task Updated",

            user_id=current_user.id
        )

        db.session.add(history)

        db.session.commit()

        socketio.emit(

            "notification",

            {
                "message": f"Task Updated: {task.title}"
            }
        )

        flash(
            "Task Updated Successfully",
            "success"
        )

        return redirect("/dashboard")

    return render_template(
        "edit_task.html",
        task=task
    )


# DELETE TASK

@task.route("/delete-task/<int:id>")

@login_required

def delete_task(id):

    task = Task.query.get_or_404(id)

    if task.user_id == current_user.id:

        task.deleted = True

        history = TaskHistory(

            task_title=task.title,

            action="Task Deleted",

            user_id=current_user.id
        )

        db.session.add(history)

        db.session.commit()

        socketio.emit(

            "notification",

            {
                "message": "Task Deleted"
            }
        )

        flash(
            "Task Deleted Successfully",
            "danger"
        )

    return redirect("/dashboard")


# DELETE HISTORY

@task.route("/delete-history/<int:id>")

@login_required

def delete_history(id):

    history = TaskHistory.query.get_or_404(id)

    db.session.delete(history)

    db.session.commit()

    flash(
        "History Deleted",
        "info"
    )

    return redirect("/dashboard")


# EXPORT CSV

@task.route("/export-csv")

@login_required

def export_csv():

    tasks = Task.query.filter_by(

        user_id=current_user.id,

        deleted=False

    ).all()

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow([

        "Title",

        "Description",

        "Priority",

        "Status",

        "Deadline",

        "Created Date"
    ])

    for task in tasks:

        writer.writerow([

            task.title,

            task.description,

            task.priority,

            task.status,

            task.deadline,

            task.created_date
        ])

    response = make_response(
        output.getvalue()
    )

    response.headers[
        "Content-Disposition"
    ] = "attachment; filename=tasks.csv"

    response.headers[
        "Content-type"
    ] = "text/csv"

    return response


# GET ALL TASKS API

@task.route("/api/tasks")

@login_required

def get_tasks():

    tasks = Task.query.filter_by(

        user_id=current_user.id,

        deleted=False

    ).all()

    task_list = []

    for task in tasks:

        task_list.append({

            "id": task.id,

            "title": task.title,

            "description": task.description,

            "priority": task.priority,

            "status": task.status,

            "deadline": task.deadline,

            "created_date": str(task.created_date)
        })

    return jsonify(task_list)