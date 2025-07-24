from flask import Flask
from routes.users import user_bp
from init_db import init_db

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    # Initialize DB
    init_db()

    # Register Blueprint
    app.register_blueprint(user_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
