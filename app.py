from flask import Flask
from threading import Thread
import tw_code

Thread(target=tw_code.run).start()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'pong'


if __name__ == "__main__":
    app.run()
