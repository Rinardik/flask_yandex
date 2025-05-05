from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from data.db_session import SqlAlchemyBase
from data.users import User
from sqlalchemy.orm import relationship

class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    job_title = Column(String, nullable=False)
    team_leader_id = Column(Integer, ForeignKey('users.id'))
    work_size = Column(Integer)
    collaborators = Column(String)
    is_finished = Column(Boolean)
    team_leader = relationship("User", back_populates="jobs")