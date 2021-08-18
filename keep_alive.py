from flask import Flask, jsonify, request
from threading import Thread
import os
app = Flask('')

@app.route("/")
def home():
	return jsonify({"status":True})


"""
WIP: LOADING CODE FROM GITHUB
@app.route("/update", methods=["POST"])
def update():
	if request.json
"""

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()