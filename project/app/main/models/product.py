from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey,
                        BigInteger, String)

from app.main import db
from .stock import stock_table


class Product(db.Model):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True)
    sku = Column(String(16), index=True)
    name = Column(String())
    image = Column(String())
    stores = relationship(
        'Store',
        secondary=stock_table,
        back_populates='products'
    )

    def __init__(self, id, sku, name, image):
        self.id = id
        self.sku = sku
        self.name = name
        self.image = image

    def __repr__(self):
        return '<id {}> {}'.format(self.id, self.name)
