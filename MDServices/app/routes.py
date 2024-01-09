# /app/routes.py

from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app.models import User
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('artisan_services'))
    return render_template('login.html', form=form)

# Add other routes and functionalities as needed
