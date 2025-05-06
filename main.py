from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
import datetime

DB_NAME = "db/blog.db"
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String, nullable=False)
    age = Column(Integer)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.now)
    is_finished = Column(Boolean, default=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

def init_db():
    engine = create_engine(f"sqlite:///{DB_NAME}?check_same_thread=False")
    Base.metadata.create_all(engine)
    return engine

if __name__ == "__main__":
    engine = init_db()
    Session = sessionmaker(bind=engine)
    db_sess = Session()
    captain_email = "scott_chief@mars.org"
    if not db_sess.query(User).filter(User.email == captain_email).first():
        captain = User(
            surname="Scott",
            name="Ridley",
            age=21,
            position="captain",
            speciality="research engineer",
            address="module_1",
            email=captain_email
        )
        captain.set_password("password")
        db_sess.add(captain)
        print("Капитан добавлен")
    colonists = [
        {
            "surname": "Watney",
            "name": "Mark",
            "age": 35,
            "position": "biologist",
            "speciality": "botanist",
            "address": "module_2",
            "email": "watney@mars.org"
        },
        {
            "surname": "Lewis",
            "name": "Melissa",
            "age": 38,
            "position": "commander",
            "speciality": "geologist",
            "address": "module_3",
            "email": "lewis@mars.org"
        },
        {
            "surname": "Purnell",
            "name": "Bruce",
            "age": 45,
            "position": "mission director",
            "speciality": "aerospace engineer",
            "address": "Earth control",
            "email": "purnell@mars.org"
        }
    ]
    for col in colonists:
        if not db_sess.query(User).filter(User.email == col["email"]).first():
            user = User(**col)
            user.set_password("password")
            db_sess.add(user)
            print(f"Добавлен {col['name']} {col['surname']}")
    db_sess.commit()
    print("Все пользователи успешно добавлены в базу данных.")