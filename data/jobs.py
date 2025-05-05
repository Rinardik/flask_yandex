from .db_session import SqlAlchemyBase
import sqlalchemy

class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    job_title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    team_leader_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    work_size = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, default='')
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)