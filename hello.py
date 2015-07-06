# coding=UTF-8

# @brief {brief description]
#
# @author webofthink@snu.ac.kr
#
# from http://flask.pocoo.org/ tutorial
from flask import Flask
app = Flask(__name__)

@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
