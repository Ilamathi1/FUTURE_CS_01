from flask import Flask, request, render_template, redirect, url_for
from auth import generate_qr_code, register_user, authenticate_user, verify_totp
from models import db, User

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        secret_key = register_user(username, password)
        qr_code = generate_qr_code(secret_key, username, 'SampleApp')
        return render_template('register.html', qr_code=qr_code)
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_totp = request.form['totp']
        
        user = authenticate_user(username, password)
        if user and verify_totp(user.secret_key, user_totp):
            return "Login successful!"
        else:
            return "Invalid credentials. Please try again."
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)