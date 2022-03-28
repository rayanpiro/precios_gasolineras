from flask import Flask, render_template
from backend.controller.flask_http_controller import gs

app = Flask(__name__, template_folder='./frontend/', static_folder='./frontend/static')
app.register_blueprint(gs)

@app.get('/') # type: ignore
def index():
    return render_template("index.html")