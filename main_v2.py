import datetime

from flask import Flask, render_template
from flask_login import LoginManager
from flask_restful import reqparse, abort, Api, Resource
# noinspection PyUnresolvedReferences
from data import news_resources
# noinspection PyUnresolvedReferences
from data import db_session
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
api = Api(app)
login_manager.init_app(app)

def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    db_sess = db_session.create_session()

    @app.route('/')
    def index():
        return render_template('index.html')
    app.run()


if __name__ == '__main__':
    main()