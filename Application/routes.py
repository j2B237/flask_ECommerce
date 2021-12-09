""" Application routes module """

# Third party import
from flask import render_template

# Local party import
from Application import app


@app.route("/")
def index():
    return render_template("index.html", title="Sen Shop")


@app.route("/account")
def account():
    return "Account view"


@app.route("/wishlist")
def wishlist():
    return "wishlist view"


@app.route("/cart")
def cart():
    return "cart view"


@app.route("/checkout")
def checkout():
    return "checkout view"


@app.route("/login")
def login():
    return "Login view"
