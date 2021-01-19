from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey,
                        BigInteger, String)

from app.main import db
from .stock import stock_table


class Store(db.Model):
    __tablename__ = 'stores'
    id = Column(BigInteger, primary_key=True)
    name = Column(String())
    phone = Column(String())
    email = Column(String(), index=True, unique=True)
    street = Column(String())
    external_number = Column(String())
    internal_number = Column(String())
    postal_code_id = Column(
        BigInteger,
        ForeignKey('postal_codes.id'),
        index=True
    )
    store_pcode = relationship(
        'PostalCode',
        backref='pcode_stores'
    )
    products = relationship(
        'Product',
        secondary=stock_table,
        back_populates='stores',
    )

    def __init__(self, name, phone, email,
                 street, external_number, internal_number,
                 postal_code_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.street = street
        self.external_number = external_number
        self.internal_number = internal_number
        self.postal_code_id = postal_code_id

    def __repr__(self):
        return '<id {}> {}'.format(self.id, self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True
