from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/ping")
def ping():
    return "pong"


if __name__ == '__main__':
    app.run(None, 15000, True)
