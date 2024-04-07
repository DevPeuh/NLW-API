from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Events(Base):
    __tablename__ = 'events'
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True) #coluna que se chama id, é uma string, também uma chave primaria!
    title = Column(String, nullable=False) #ele não pode ser nulo -> 'nullable=False'
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        return f'Events [title={self.title}, maximum_attendees={self.maximum_attendees}'