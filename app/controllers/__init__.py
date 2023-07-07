from app import app
from flask import request,  url_for, redirect, render_template
from requests import get, post
from colorama import Fore, Style

class FireWar:
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
    
    def home(self):
        if self.name == 'Zezo':
            render_template('index.html')