""" Application routes module """

# Third party import
from flask import render_template

# Local party import
from Application import app


@app.route("/")
def index():
    return render_template("index.html", title="Sen Shop")
