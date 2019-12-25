from flask import Flask
from core.emailsender import EmailSender
from concurrent.futures import ThreadPoolExecutor
from core.servermonitor import background_process

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    executor = ThreadPoolExecutor(1)
    executor.submit(background_process)

    app.run()
