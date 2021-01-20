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
    pcodes_store = relationship(
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

    @staticmethod
    def get_pagination(limit=100, offset=0):
        query = PostalCode.query.order_by(
            PostalCode.id.asc()
        ).limit(limit).offset(offset)
        return query
