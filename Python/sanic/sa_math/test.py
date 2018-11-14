from sanic import Blueprint
import sanic.response as res
import authorized

bp = Blueprint(__name__, url_prefix='/math')


@bp.route("/")
@authorized.authorized
async def sindex(request):
    return res.text("Hello World!")
