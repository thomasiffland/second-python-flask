from flask import Flask
from flask import jsonify
app = Flask(__name__)



@app.route('/fib/<num>', methods=['GET'])
def fib_handler(num):
    return jsonify(fib(int(num)))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    app.run()
