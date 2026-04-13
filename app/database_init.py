from app.database import engine, Base
from app.models.user import User  # noqa: F401 - import to register model with Base

def init_db():
    Base.metadata.create_all(bind=engine) # pragma: no cover # bind the metadata to the engine and create all tables defined by the models that inherit from Base

def drop_db():
    Base.metadata.drop_all(bind=engine) # pragma: no cover # bind the metadata to the engine and drop all tables defined by the models that inherit from Base

if __name__ == "__main__":
    init_db() # pragma: no cover