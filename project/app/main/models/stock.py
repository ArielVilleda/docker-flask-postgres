from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey,
                        BigInteger, Integer, String)

from app.main import db


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = Column(BigInteger, primary_key=True)
    store_id = Column(BigInteger, ForeignKey('stores.id'))
    product_id = Column(BigInteger, ForeignKey('products.id'))
    sku = Column(String(), nullable=False, unique=True, index=True)
    store = relationship("Store", back_populates="products")
    product = relationship("Product", back_populates="stores")

    def __repr__(self):
        return '<store: {}, product: {}> {}'.format(
            self.store_id,
            self.product_id,
            self.sku
        )
