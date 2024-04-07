import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import Eventsrepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='não necessário') # vai pular o de baixo e partir para o próximo
def test_insert_event():
    event = {
        'uuid': 'meu-uui-e-nois',
        'title': 'meu titulo',
        'slug': 'meu-slug-aqui',
        'maximum_attendees': 20
    }
    
    events_repository = Eventsrepository()
    resp = events_repository.insert_event(event)
    print(resp)

def test_get_event_by_id():
    event_id = 'meu-uui-e-nois'
    events_repository = Eventsrepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    print(response.title)
