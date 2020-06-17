# Flask documentation: https://flask.palletsprojects.com/en/1.1.x/

from flask import Flask, jsonify
from scraper import get_data

app = Flask(__name__)


@app.route('/headlines', methods=['POST'])
def headline_api():
    try:
        data = get_data()
        response = jsonify(data)  # this should be a python dict
        return response
    except:
        # handle error
        return 'Error'
