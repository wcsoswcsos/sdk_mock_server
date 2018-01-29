import pdb
import sdk_server
import sdk_dataplatform
from flask import Flask,request,make_response
from config import basic_config
pdb.set_trace()
app = Flask('__name__')


@app.route('/')
def index():
    return 'this is a mock server'

app.register_blueprint(sdk_server.bp_sdkserver,url_prefix='/sdkserver')
app.register_blueprint(sdk_dataplatform.bp_dataplatform,url_prefix='/dataplatform')

if __name__ == '__main__':
    HOST = '172.18.12.3'
    if HOST in ['localhost','127.0.0.1']:
        app.debug=True
    # app.run(host=HOST)
    app.run(host=HOST)