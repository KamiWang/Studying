from sanic import Blueprint
import exception as expt
from common import CommonReply

bp = Blueprint(__name__, url_prefix='')


@bp.route("/radixConvert")
async def radix_convert(request):
    return CommonReply().json
