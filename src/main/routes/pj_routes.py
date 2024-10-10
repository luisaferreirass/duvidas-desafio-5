from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pj_creater_composer import pj_creator_composer
from src.main.composer.pj_lister_composer import pj_lister_composer

pj_routes_bp = Blueprint("pj_routes", __name__)

@pj_routes_bp.route("/pessoajuridica", methods=["POST"])
def create_pj():
    http_request = HttpRequest(body= request.json)
    view = pj_creator_composer()

    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pj_routes_bp.route("/pessoajuridica", methods=["GET"])
def list_pj():
    http_request = HttpRequest()
    view = pj_lister_composer()

    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
