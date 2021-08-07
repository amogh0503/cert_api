from flask import Flask, request, jsonify
import json
app = Flask(__name__)
@app.route('/hello/', methods=['POST'])
def welcome():
    input_data = request.json["Name"]
    return input_data
if __name__ == '__main__':
    app.run(host='localhost', port=105)