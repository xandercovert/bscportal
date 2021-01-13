from flask import Flask, render_template, url_for, redirect, flash, request, jsonify
import sys
import os
import time
import secrets
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_killed_my_father_prepare_to_die'
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)