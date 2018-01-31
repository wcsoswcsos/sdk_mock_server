from . import actions
from flask import Blueprint

bp_sdkserver = Blueprint('sdkserver','__name__')

#meitu.com
@bp_sdkserver.route('/lua/report/report.json')
def _report():
    return actions.report_data()

@bp_sdkserver.route('/lua/advertv3/getload.json')
def _get_load():
    return actions.load_data()

@bp_sdkserver.route('/lua/advertv3/getpreload.json')
def _get_preload():
    return actions.preload_data()

@bp_sdkserver.route('/lua/advertv3/gets2s.json')
def _get_s2s():
    return actions.s2s_data()

@bp_sdkserver.route('/lua/advertv3/getfilterapp.json')
def _get_filter_app():
    return actions.filterapp_data()

@bp_sdkserver.route('/lua/advertv3/getsetting.json')
def _get_setting():
    return actions.setting_data()

@bp_sdkserver.route('/lua/advertv3/getwebview.json')
def _get_web_view():
    return actions.webview_data()