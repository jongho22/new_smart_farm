from flask import Flask, Response, render_template
from pymongo import MongoClient
from datetime import datetime
import json
import time
import random

app = Flask(__name__)

my_client = MongoClient("mongodb://localhost:27017/")

db = my_client['Measurement']
db_col = db.data

#@app.route('/')
#def graph():
#    return render_template('graph.html')

#@app.route('/graph')
#def chart_data():
#    def generate_raw_data():
#        while True:
#            raw_data = db.col.find().sort("_id",-1).limit(1)