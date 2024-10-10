from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pf_creator_composer import pf_creator_composer
from src.main.composer.pf_lister_composer import pf_lister_composer


pf_route_bp = Blueprint("pf_routes", __name__)

@pf_route_bp.route("/pessoafisica", methods=["POST"])
def pf_create():
    
    http_request = HttpRequest(body= request.json)
    view = pf_creator_composer()

    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
    
@pf_route_bp.route("/pessoafisica", methods=["GET"])
def pf_list():
    http_request = HttpRequest()
    view = pf_lister_composer()

    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
