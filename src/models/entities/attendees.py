from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class Attendees(Base):
    __tablename__ = 'attendees'
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey('events.id'))
    checked_in_at = Column(DateTime) 
    created_at = Column(DateTime, default=func.now())
    
    def __str__(self):
        return f'Attendees [name={self.name}, email = {self.email}, event_id = {self.event_id}]'
    
