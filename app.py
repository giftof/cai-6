"""
this is module docstring
"""


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    this is function docstring
    """
    return 'Hello, DevOps!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
