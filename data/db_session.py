import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

# абстрактная модель БД
SqlAlchemyBase = dec.declarative_base()
# сессия для подключения к БД
__factory = None
# принимает на вход адрес базы данных, затем проверяет, не создали ли мы уже фабрику подключений:
def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")
# check_same_thread=False — заставляет подключение не проверять,
    # что разные объекты получаются из базы данных в разных нитях исполнения Python
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False' # тип базы данных, адрес до базы данных и параметров подключения
    print(f"Подключение к базе данных по адресу {conn_str}")
    #  движок работы с базой данных
    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)
# тут SQLalchemy узнает о всех наших моделях
    from . import __all_models
# заставляем нашу базу данных создать все объекты, которые она пока не создала:
    SqlAlchemyBase.metadata.create_all(engine)

def create_session() -> Session:
    global __factory
    return __factory()

