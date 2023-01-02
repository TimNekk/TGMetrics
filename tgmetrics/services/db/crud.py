from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from tgmetrics.config import load_config

Base = declarative_base()

config = load_config()

engine = create_engine(config.db.uri)

Session = sessionmaker(bind=engine)


def recreate_database() -> None:
    print(Base.metadata.tables)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
