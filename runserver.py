# from flask import Flask
# from flask import render_template, request, redirect, url_for
from src import app


if __name__ == "__main__":
    app.run('localhost', '8080')