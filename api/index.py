from flask import Flask, request,jsonify,send_from_directory
from flask_cors import CORS

from model_food import recommend_foods
from model_stunting import predict_status_gizi

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

