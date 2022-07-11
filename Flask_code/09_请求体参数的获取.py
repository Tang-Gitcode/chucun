from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    return f"hello=={uname}=={pwd}"

if __name__ == '__main__':
    app.run(debug=True)