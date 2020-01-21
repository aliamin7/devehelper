from datetime import datetime
from .. import app
from flask import render_template, request, redirect, url_for


@app.route('/login')
# @login_required
def login():
    return render_template(
        'login.html',
        year=datetime.now().year)