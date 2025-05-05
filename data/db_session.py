import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
SqlAlchemyBase = orm.declarative_base()


__engine = None
__session_factory = None


def global_init(db_file: str):
    global __engine, __session_factory

    if __session_factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("db/blog.db")

    conn_str = f'sqlite:///{db_file}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    __engine = sa.create_engine(conn_str, echo=False)
    __session_factory = orm.sessionmaker(bind=__engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(__engine)


def create_session() -> Session:
    if __session_factory is None:
        raise Exception("Вы не вызвали global_init() перед использованием сессии!")
    return __session_factory()