from selectors import BaseSelector
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class liConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

app.url_map.converters['li'] = liConverter

@app.route("/")
def index():
    return "hello"

@app.route("/user/<info>")
def user(info):

    args = info.split('+')
    return f"获取了某某的信息{args}"

@app.route("/user_info/<li:info>")
def user_info(info):

    # args = info.split('+')
    return f"获取了某某的信息{info}"


if __name__ == "__main__":
    app.run(debug=True)