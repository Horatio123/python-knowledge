from flask import Flask
from flask import request

app = Flask(__name__)

"""
flask --app flask_test run
gunicorn -w 5 -b 127.0.0.1:6000 flask_test:app
"""


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test_post", methods=["POST", 'GET'])
def hello_post():
    print(request.method)
    # print(request.args)
    # print(request.form)
    print(request.get_data())
    print(request.get_json())
    user = request.get_json()['user']
    print(user)

    return request.get_data()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
