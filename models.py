from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return f'<Task {self.title!r}>'
