import requests
from flask import Flask, request
import numpy as np
from flask import jsonify
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/images'



@app.route('/generate/<num>', methods=['GET'])
def generate(num):
    random_nums = np.random.randint(100000, size=int(num))
    return jsonify(random_nums.tolist())


@app.route('/generate/<num>/sorted', methods=['GET'])
def generate_sorted(num):
    random_nums = np.random.randint(100000, size=int(num))
    r = requests.post('http://sort:9091/sort',json=random_nums.tolist())
    return jsonify(r.json())


@app.route('/generate/<num>/sorted/reverse', methods=['GET'])
def generate_sorted_reverse(num):
    random_nums = np.random.randint(100000, size=int(num))
    r = requests.post('http://sort:9091/sort/reverse', json=random_nums.tolist())
    return jsonify(r.json())


# @app.route('/resize/percent', methods=['POST'])
# def resizePercent():
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])
#     file = request.files['file']
#     percent = request.values['percent']
#     if file:
#         extension = os.path.splitext(file.filename)[1]
#         path = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()))
#         file.save(path + extension)
#         url = 'http://exifdata:8082/exifdata/filtered'
#         files = {'file': open(path+extension, 'rb')}
#
#         r = requests.post(url, files=files, data={'filter': 'Image Height'})
#
#         percentSize = float(str(r.text).split(':')[1].strip()) * (float(percent) / 100)
#
#         resized = resizeCmd(path, extension, str(percentSize)+'x'+str(percentSize))
#         return send_file(resized, mimetype="image/*")
#
#
#
# def resizeCmd(path, extension, size):
#     newFileName = path + "_resized" + extension
#     subprocess.call(('convert', path + extension,"-resize", size, newFileName))
#     return newFileName;

if __name__ == '__main__':
    app.run()
