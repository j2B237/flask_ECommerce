""" Application factory """

# Third party import
from flask import Flask

# Local party import
from instance.config import config

app = Flask(__name__)
app.config.from_object(config["development"])


@app.route("/")
def index():
    return "Hello World by Flask"
