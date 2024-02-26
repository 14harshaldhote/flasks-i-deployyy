from flask import Flask, jsonify
from app import app

@app.route('/api/', methods=['GET'])
def api_index():
    return jsonify({'message': 'Welcome to the API!'})

# Add more endpoints here if needed

