from datetime import datetime

from models.extensions import db


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    priority = db.Column(db.String(50), nullable=False)

    status = db.Column(
        db.String(50),
        default="Pending"
    )

    deadline = db.Column(db.String(100))

    created_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    deleted = db.Column(
        db.Boolean,
        default=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )


# TASK HISTORY TABLE

class TaskHistory(db.Model):

    __tablename__ = "task_history"

    id = db.Column(db.Integer, primary_key=True)

    task_title = db.Column(
        db.String(200)
    )

    action = db.Column(
        db.String(100)
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )