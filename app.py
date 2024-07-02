import requests

from flask import Flask, jsonify, request, redirect
app = Flask(__name__)

API_URL = 'https://2710.in:8443/api'
TOKEN = "20a55321-9b64-4b51-8d7d-2c83d06b2657"

ip_whitelist = [
    "127.0.0.1" # localhost,
    "157.47.18.238",
]

tokens = [
    "tony-stark",
    "captain-america",
]

@app.route('/')
def root_func():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return {
        "ip": ip,
        "whitelisted": ip in ip_whitelist
    }

@app.route('/chrome', methods=["POST"])
def chromeapi():
    # IP Whilelisting
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if ip not in ip_whitelist:
        return {"status": 403, "error": "Access forbidden."}
    
    # Token check
    if post_json["token"] not in tokens:
        return {"status": 403, "error": "Invalid Token."}

    post_json = request.json
    post_json["token"] = TOKEN
    r3 = requests.post(API_URL, json=post_json)
    return r3.json()

app.run(port=8081)
