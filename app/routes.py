from flask import Blueprint, render_template
from app.dashboard_embed import get_dashboard_html

main = Blueprint('main', __name__)

@main.route("/")
def index():
    dashboard_html = get_dashboard_html()
    return render_template("index.html", dashboard_html=dashboard_html)
