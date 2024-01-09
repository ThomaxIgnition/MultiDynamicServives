# app.py
from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
# app/__init__.py

login_manager = LoginManager(app)
login_manager.login_view = 'login'
csrf = CSRFProtect(app)

from app import routes
