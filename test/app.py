from flask import Flask, request
import os
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
    with open("app.py", "r+") as f:
        return f.read()


@app.route("/shell", methods=['POST'])
def shell():
    action = request.form["act"]
    app.logger.info('action is :%s', action)
    if action.find(" ") != -1:
        return "Nonono"
    else:
        os.system(action)
    return "Wow"


@app.errorhandler(404)
def error_date(error):
    sleep(5)
    return "扫扫扫，扫啥东方明珠呢[怒]"


if __name__ == "__main__":
    app.run()
