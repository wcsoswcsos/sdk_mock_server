import pdb
import sdk_server
import material_server
from flask import Flask,request,make_response
from config import basic_config
app = Flask('__name__')

@app.before_request
def before_request():
    pdb.set_trace()
    app.logger.debug('new request')

@app.route('/')
def index():
    return 'this is a mock server'

app.register_blueprint(sdk_server.bp_sdkserver)
if __name__ == '__main__':
    HOST = '172.18.12.3'
    if HOST in ['localhost','127.0.0.1']:
        app.debug=True
    app.run(host=HOST)