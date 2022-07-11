from flask import Flask

app = Flask(__name__)

# @app.route("/index/home/274928759823")
# def index1():
#     return "hello"

# @app.route("/index/home/123123")
# def index2():
#     return "1274729171"


@app.route("/index/home/<id>")
def index(id):

    print (f"接收到的id是：{id}")
    return f"返回了{id}的文章"


if __name__ == "__main__":
    app.run(debug=True)