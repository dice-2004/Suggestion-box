from flask import Flask
import os
from views import view

app= Flask(__name__)


app.register_blueprint(view)
