from flask import Flask, request, jsonify
import json
app = Flask(__name__)
@app.route('/hello/', methods=['POST'])
def welcome():
    input_data = request.json["Name"]
    return input_data

@app.route('/v1/send_cert',methods=['GET'])
def get_params():       # only accepts first parameter of url paramaters
    queryString = request.args  #For Signature Given
    Title = request.args.get('Title')
    Name = request.args.get('Name')
    Body = request.args.get('Body')
    Date = request.args.get('Date')
    Signature = request.args.get('Signature',None)  #optional parameter in url
    Link = request.args.get('Link')
    return queryString

if __name__ == '__main__':
    app.run(host='localhost',debug=True, port=105)