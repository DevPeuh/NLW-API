import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo regstro em banco de dados')
def test_insert_attendee():
    event_id = 'meu-uui-e-nois'
    attendees_info = {
        'uuid': 'meu_uuid_attendee',
        'name': 'atendee name',
        'email': 'email@email.com',
        'event_id': event_id
    }
    Attendees_Repository = AttendeesRepository()
    response = Attendees_Repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason='. . .')
def test_get_attendee_badge_by_id():
    attendde_id = 'meu_uuid_attendee'
    Attendees_Repository = AttendeesRepository()
    attendee = Attendees_Repository.get_attendee_badge_by_id(attendde_id)

    print(attendee)
    print(attendee.title)