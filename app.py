from flask import Flask
from flask_smorest import Api

from model.response.implementation.response.simple_info_response import SimpleInfoResponse
from model.response.implementation.payload.simple_message_payload import SimpleMessagePayload
from route.system_route import system_blueprint as SystemBlueprint

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return SimpleInfoResponse(SimpleMessagePayload("Hello FlaskBerry")).to_json()


@app.route('/h')
def hello_world_2():  # put application's code here
    return SimpleInfoResponse(SimpleMessagePayload("Hello FlaskBerry2")).to_json()


if __name__ == '__main__':
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "FLASKBERRY"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdeliver.net/npm/swagger-ui-dist/"
    api = Api(app)
    api.register_blueprint(SystemBlueprint)
    app.run()
