from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url= "postglresql://postgres:postgres@localhost:5432/pos_db"

engine = create_engine(database_url, echo=False, future=True)
Session =sessionmaker(autocommit=False, autoflash=False)
Base=declarative_base()


def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()
    