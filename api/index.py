from flask import Flask, jsonify
from app import app, get_google_sheet_data

@app.route('/api/get_sheet_data', methods=['GET'])
def api_get_sheet_data():
    data = get_google_sheet_data()
    return jsonify({'data': data})
