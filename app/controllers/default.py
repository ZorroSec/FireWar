from app import app
from flask import Flask, request, url_for, render_template
from requests import get, post
from app.controllers import FireWar
from colorama import Fore, Style

name = input(f'{Fore.RE}')

@app.route('/', methods=['GET', 'POST'])
def home():
    RE