from flask import Flask
from data import data
app = Flask(__name__)

@app.route('/test')
def generate_test_response():
    response = data.DataGenerator()

    return {
        "response" : response.name,
        "time": response.time
    }
