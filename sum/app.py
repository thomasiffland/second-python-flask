import requests
from flask import Flask, request
import numpy as np
from flask import jsonify
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/images'



@app.route('/sum', methods=['POST'])
def sum_handler():
    list_to_sum: list = request.get_json()
    return jsonify(sum(list_to_sum))


@app.route('/sum/<num>', methods=['GET'])
def sum_with_num(num):
    r = requests.get('http://generate:9090/generate/'+num)
    list_to_sum: list = r.json()
    return jsonify(sum(list_to_sum))




if __name__ == '__main__':
    app.run()
