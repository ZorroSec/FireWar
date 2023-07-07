from app import app
from flask import Flask
from colorama import Fore

name = input(f'{Fore.LIGHTBLACK_EX}[*] {Fore.LIGHTBLUE_EX}=+> {Fore.RED}')
password = input(f'{Fore.LIGHTBLACK_EX}[*] {Fore.LIGHTBLUE_EX}=+> {Fore.RED}')

if password == "Zezao":
    if __name__ == '__main__':
        app.run(
            debug=True
        )