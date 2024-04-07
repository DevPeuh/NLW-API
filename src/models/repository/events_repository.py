from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError

class Eventsrepository:
    def insert_event(self, eventsinfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                event = Events(
                    id = eventsinfo.get('uuid'), # uudi -> é uma estrutura de identidade na base de textos
                    title = eventsinfo.get('title'),
                    details = eventsinfo.get('details'),
                    slug = eventsinfo.get('slug'),
                    maximum_attendees = eventsinfo.get('maximum_attendees'),
                )
                database.session.add(event)
                database.session.commit()

                return eventsinfo # isso tudo acima para inserir um elemento dentro do banco
            except IntegrityError:
                raise HttpConflictError('Evento já cadastrado!')

            except Exception as exception:
                database.session.rollback() # Se der erro volta para o estado anterior
                raise exception # faz o roll back e levanta a sessão de qualquer forma

    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
            try:
                event = (
                    database.session
                        .query(Events)
                        .filter(Events.id == event_id)
                        .one()
                )
                return event
            except NoResultFound:
                return None

    def count_event_attendees(self, event_id: str) -> Dict:
        with db_connection_handler as database:
            try:
                event_count = (
                    database.session
                        .query(Events)
                        .join(Attendees, Events.id == Attendees.event_id)
                        .filter(Events.id == event_id)
                        .with_entities(
                            Events.maximum_attendees,
                            Attendees.id
                        )
                        .all() # Vai buscar todos que tiver as condições acima
                )
                if not len(event_count): # se ninguém for encontrado
                    return {
                        'maximumAttendees': 0,
                        'attendeesAmount': 0
                    }
                return {
                    'maximumAttendees': event_count[0].maximum_attendees,
                    'attendeesAmount': len(event_count) # Quantidade de pessoas cadastradas no evento
                }
            except:
                pass