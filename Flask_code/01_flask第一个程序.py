from flask import Flask


app = Flask(__name__)

@app.route("/index")
def index():
    return "hello"


if __name__ == "__main__":
    # app.run()
    app.run(port=8000)