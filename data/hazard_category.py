from sqlalchemy import Column, Integer, String
from data.db_session import SqlAlchemyBase


class HazardCategory(SqlAlchemyBase):
    __tablename__ = 'hazard_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)