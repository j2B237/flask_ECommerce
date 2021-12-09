""" Application factory """

# Third party import
from flask import Flask

# Local party import
from instance.config import config

app = Flask(__name__)
app.config.from_object(config["development"])

from Application import routes