from flask import Flask
from backend.controller.flask_http_controller import gs

app = Flask(__name__)
app.register_blueprint(gs)