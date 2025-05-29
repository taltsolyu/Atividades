from config import app, db
from controllers.atividade_controller import atividades_api

app.register_blueprint(atividades_api, url_prefix='/atividades')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )