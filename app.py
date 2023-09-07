import requests
import json
import time
import re
from pymongo import MongoClient
import datetime
from flask import Flask
from flask import abort, redirect, url_for, request, jsonify, Markup


dbhost = 'mongodb://' + settings['dbuser'] + ':' + settings['dbpass'] + settings['dbhost']


def CreateShow(name):


app = Flask(__name__)

@app.route("/")
def 
