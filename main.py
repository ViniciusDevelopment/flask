import os
import json
import mimetypes
from flask import Flask, Response, jsonify
from itertools import combinations
from itertools import combinations
import numpy as np
from pandas import DataFrame
from IPython.display import display
from statistics import variance
from scipy.stats import t, f, norm
import matplotlib.pyplot as plt
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}})



# from flask import Flask, jsonify
# import os

# app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
