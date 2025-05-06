from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    city_from = Column(String, default="Москва")
    jobs = relationship("Job", back_populates="team_leader")
    def to_dict(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'speciality': self.speciality,
            'address': self.address,
            'email': self.email,
            'hashed_password': self.hashed_password,
            'city_from': self.city_from
        }