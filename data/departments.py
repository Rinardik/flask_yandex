from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey('users.id'), nullable=False)
    members = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    leader = relationship("User")