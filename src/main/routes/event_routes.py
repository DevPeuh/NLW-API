from flask import Blueprint, jsonify, request # jsonify - Ajuda a dar nomes para os decoradores das rotas
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler
from src.errors.error_types.error_handler import handle_error

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods = ['POST'])
def create_event():
    try:
        http_request = HttpRequest(body = request.json) # Vai tirar a informação do framework para o padrão q está utilizando -> 'HttpRequest'
        event_handler = EventHandler()


        http_response = event_handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code # Para conseguir transformar elementos em json e testar se funciona
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        event_handler = EventHandler()
        http_request = HttpRequest(param={ "event_id": event_id })
        
        http_response = event_handler.finf_by_id(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code