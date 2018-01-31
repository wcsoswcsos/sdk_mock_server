from flask import Blueprint

bp_dataplatform = Blueprint('datapltform','__name__')

#大数据平台接口
@bp_dataplatform.route('/plain')
def plain():
    return 'plain'

