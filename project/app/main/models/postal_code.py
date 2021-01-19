from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey,
                        BigInteger, String)

from app.main import db


class PostalCode(db.Model):
    __tablename__ = 'postal_codes'
    id = Column(BigInteger, primary_key=True)
    neighborhood = Column(String())
    district = Column(String())
    state = Column(String())
    city = Column(String())
    postal_code = Column(String(), index=True)
    pcodes_stores = relationship(
        'Store',
        backref='postal_code'
    )

    def __init__(self, neighborhood, district, state,
                 city, postal_code):
        self.neighborhood = neighborhood
        self.district = district
        self.state = state
        self.city = city
        self.postal_code = postal_code

    def __repr__(self):
        return '<id: {}> {}'.format(self.id, self.postal_code)
