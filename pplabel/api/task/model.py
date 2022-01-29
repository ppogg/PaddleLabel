from datetime import datetime

from sqlalchemy.orm import backref

from pplabel.config import db
from ..util import nncol
from ..data.model import Data
from ..annotation import Annotation
from ..project import Project


class Task(db.Model):
    __tablename__ = "task"
    __table_args__ = {"comment": "Contains all the tasks"}
    task_id = nncol(db.Integer(), primary_key=True)
    project_id = nncol(
        db.Integer(), db.ForeignKey("project.project_id", ondelete="CASCADE")
    )
    project = db.relationship("Project")
    datas = db.relationship("Data", backref="task", lazy="selectin")
    annotations = db.relationship("Annotation", backref="task", lazy="selectin")
    created = nncol(db.DateTime, default=datetime.utcnow)
    modified = nncol(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # def __init__(self, project_id):
    #     project_id = project_id
