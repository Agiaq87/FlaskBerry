from flask import Flask
from flask_smorest import Api

from di.persistence.persistence_manager import PersistenceManager
from model.response.implementation.payload.simple_message_payload import SimpleMessagePayload
from model.response.implementation.response.standard_info_response import StandardInfoResponse
from route.system.system_http_counter import system_http_counter_blueprint as system_http_counter_blueprint
from route.system.system_route import system_blueprint as system_blueprint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "FLASKBERRY"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdeliver.net/npm/swagger-ui-dist/"
app.config['ZODB_STORAGE'] = 'file://persistenceFlaskBerry.fs'
api = Api(app)
api.register_blueprint(system_blueprint)
api.register_blueprint(system_http_counter_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return StandardInfoResponse(SimpleMessagePayload("Hello FlaskBerry")).to_json()


@app.route('/h')
def hello_world_2():  # put application's code here
    return StandardInfoResponse(SimpleMessagePayload("Hello FlaskBerry2")).to_json()


if __name__ == '__main__':
    PersistenceManager().setup_db()
    app.run(debug=True)
