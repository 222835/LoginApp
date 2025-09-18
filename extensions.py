from models import get_engine, get_session

class DBManager:
    def __init__(self):
        self.engine = None

    def init_app(self, app):
        self.engine = get_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        return self.engine

    def session(self):
        return get_session(self.engine)

db = DBManager()
