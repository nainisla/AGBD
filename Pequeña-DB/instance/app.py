from flask import Flask
from config import Config, db
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(routes)

with app.app_context():
    db.create_all()
# Esto crea las tablas en la base de datos si no existen

if __name__ == '__main__':
    app.run(debug=True)