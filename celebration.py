from flask import Flask
from apps.main.auth import auth
from apps.center import centers

app = Flask(__name__)
app.register_blueprint(centers, url_prefix='')
app.register_blueprint(auth, url_prefix='/auth')


if __name__ == '__main__':
    app.run()