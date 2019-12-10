from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.debug = True
    app.run()
