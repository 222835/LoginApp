from flask import Flask
from config import Config
from extensions import db
from models import Base
from routes.auth import auth_bp
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializar base de datos
    engine = db.init_app(app)
    Base.metadata.create_all(engine)

    # registrar blueprints (rutas)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
