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
    return render_template("account.html", title="Sen Shop | Mon compte")


@app.route("/wishlist")
def wishlist():
    return render_template("wishlist.html", title="Sen Shop | Mes favoris")


@app.route("/cart")
def cart():
    return render_template("cart.html", title="Sen Shop | Mon panier")


@app.route("/checkout")
def checkout():
    return "checkout view"
