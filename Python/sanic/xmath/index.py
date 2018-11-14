from sanic import Blueprint
import exception as expt
from sanic.response import json

bp = Blueprint(__name__, url_prefix='/math')


@bp.route("/radixConvert")
async def radix_convert(request):
    number = request.args["num"][0]
    dst_radix = "10"
    if "radix" in request.args:
        dst_radix = request.args["radix"][0]

    src_radix = 10

    if number[:2] == ("0b"):
        src_radix = 2
    elif number[:2] == ("0o"):
        src_radix = 8
    elif number[:2] == ("0x"):
        src_radix = 16
    else:
        if not number.isdigit():
            raise expt.ExceptionEx(expt.ErrorCode.INVALIDE_PARAMETER, "%s not be digit or 0b,0o,0x" % number)

    dst = int(number, base=src_radix)

    if dst_radix == "2":
        dst = bin(dst)
    elif dst_radix == "8":
        dst = oct(dst)
    elif dst_radix == "16":
        dst = hex(dst)
    elif dst_radix == "10":
        dst = str(dst)
    else:
        raise expt.ExceptionEx(expt.ErrorCode.INVALIDE_PARAMETER, "radix only support:2,8,10,16")

    reply = dict()
    reply["src"] = number
    reply["src_radix"] = src_radix
    reply["dst"] = dst
    reply["dst_radix"] = dst_radix

    return json(reply)
