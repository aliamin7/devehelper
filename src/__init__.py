from flask import Flask

"""
App config
"""
app = Flask(__name__)

from src.controllers import login
