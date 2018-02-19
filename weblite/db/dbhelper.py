from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

from weblite import app

engine = create_engine(app.config['DB_URI'], convert_unicode=True, echo=True, **app.config['DB_CONN_OPTIONS'])
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def init_db():
    """ create tables inherited from base model """
    from weblite.db.staffmodel import Staff
    metadata = MetaData()
    metadata.create_all(engine)

if __name__ == '__main__':
    init_db()

