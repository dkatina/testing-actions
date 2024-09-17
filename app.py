from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})