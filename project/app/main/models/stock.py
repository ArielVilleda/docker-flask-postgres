from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey,
                        BigInteger, Integer, String)

from app.main import db


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = Column(BigInteger, primary_key=True)
    store_id = Column(BigInteger, ForeignKey('stores.id'), index=True)
    product_id = Column(BigInteger, ForeignKey('products.id'), index=True)
    sku = Column(String(), nullable=False, unique=True, index=True)
    store = relationship(
        'Store',
        back_populates='products',
        lazy='joined'
    )
    product = relationship(
        'Product',
        back_populates='stores',
        lazy='joined'
    )

    def __repr__(self):
        return '<store: {}, product: {}> {}'.format(
            self.store_id,
            self.product_id,
            self.sku
        )

    @staticmethod
    def with_relations(stock_id: int):
        query = Stock.query.options(
            db.joinedload('store'),
            db.joinedload('product')
        ).filter_by(id=stock_id)
        return query
