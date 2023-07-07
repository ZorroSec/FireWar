from app import app
from flask import Flask, request, url_for, render_template
from requests import get, post
from colorama import Fore, Style

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')