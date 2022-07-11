from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('username')
    pwd = request.args.get('pwd')
    return f"hello=={username}=={pwd}"

if __name__ == '__main__':
    app.run(debug=True)