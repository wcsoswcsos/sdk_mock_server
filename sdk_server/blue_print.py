from flask import Blueprint
from .actions import *

bp_sdkserver = Blueprint('sdkserver','__name__')

#meitu.com
@bp_sdkserver.route('/lua/report/report.json')
def report():
    return report()

@bp_sdkserver.route('/lua/advertv3/getload.json')
def get_load():
    return get_load()

@bp_sdkserver.route('/lua/advertv3/getpreload.json')
def get_preload():
    return get_preload()

@bp_sdkserver.route('/lua/advertv3/gets2s.json')
def get_s2s():
    return get_s2s()

@bp_sdkserver.route('/lua/advertv3/getfilterapp.json')
def get_filter_app():
    return get_filter_app()

@bp_sdkserver.route('/lua/advertv3/getsetting.json')
def get_setting():
    return get_setting()