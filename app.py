from flask import Flask, render_template, request, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Rate Limiter setup
limiter = Limiter(get_remote_address, app=app)

# Login Attempt Tracker
attempts = {}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
@limiter.limit("5 per 5 minutes") # Default security layer
def login():
    ip = request.remote_addr
    password = request.form.get('password')
    
    if password == "Car@2026!":
        attempts[ip] = 0
        return "Welcome to the Hypercar Database!"
    
    # Increase attempt count
    attempts[ip] = attempts.get(ip, 0) + 1
    
    if attempts[ip] >= 3:
        return "Too many failed attempts! Captcha triggered (simulated)."
        
    return "Access Denied! Incorrect password."

if __name__ == '__main__':
    app.run(debug=True)