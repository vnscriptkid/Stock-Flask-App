from flask import Flask, render_template

from app.blueprints.home import home as home_bp
from app.blueprints.stock import stock as stock_bp
from app.config import configurations


def create_app(environment_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])

    app.register_blueprint(home_bp)
    app.register_blueprint(stock_bp)

    @app.errorhandler(500)
    def handle_error(exeception):
        return render_template('500.html'), 500  # pragma: no cover

    return app


# set FLASK_APP=app:create_app('dev')
# flask run

