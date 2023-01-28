from flask import Flask, request
import os
from time import sleep

app = Flask(__name__)

flag1 = open("/tmp/flag1.txt", "r")
with open("/tmp/flag2.txt", "r") as f:
    flag2 = f.read()
tag = False


@app.route("/")
def index():
    with open("app.py", "r+") as f:
        return f.read()


@app.route("/shell", methods=['POST'])
def shell():
    global tag
    if tag != True:
        global flag1
        del flag1
        tag = True
    os.system("rm -f /tmp/flag1.txt /tmp/flag2.txt")
    action = request.form["act"]
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
