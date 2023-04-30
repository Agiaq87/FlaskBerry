from flask import Flask

from model.response.base_response import BaseResponse
from model.response.response_implementation.simple_message_payload import SimpleMessagePayload
from model.response.response_implementation.system_info_payload import SystemInfoPayload

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    b = BaseResponse(SimpleMessagePayload("Hello FlaskBerry"))
    return b.to_json()


@app.route('/h')
def hello_world_2():  # put application's code here
    b = BaseResponse(SimpleMessagePayload("Hello FlaskBerry2"))
    return b.to_json()


@app.route('/system')
def system():
    return BaseResponse(SystemInfoPayload()).to_json()


if __name__ == '__main__':
    app.run()
