from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = 'check_ins'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True) #coluna que se chama id, é uma string, também uma chave primaria!
    created_at = Column(DateTime, default=func.now())
    attendeeId =Column(String, ForeignKey('attendees.id'))


    def __repr__(self):
        return f'CheckIns [attendeeId = {self.attendeeId}]'