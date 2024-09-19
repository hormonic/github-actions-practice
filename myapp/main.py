# /home/kjm/work/ch11/ex01/github-actions-practice/myapp/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
