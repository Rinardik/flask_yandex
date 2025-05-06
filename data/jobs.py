from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from data.db_session import SqlAlchemyBase


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    job_title = Column(String(255), nullable=False)
    team_leader_id = Column(Integer, ForeignKey('users.id'))
    work_size = Column(Integer)
    collaborators = Column(String)
    is_finished = Column(Boolean)

    def to_dict(self):
        return {
            'id': self.id,
            'job_title': self.job_title,
            'team_leader_id': self.team_leader_id,
            'work_size': self.work_size,
            'collaborators': self.collaborators,
            'is_finished': self.is_finished,
            'hazard_category_id': self.hazard_category_id
        }