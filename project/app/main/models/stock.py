from sqlalchemy import (Table, Column, ForeignKey,
                        BigInteger, Integer)

from app.main import db


stock_table = Table(
    'stocks',
    db.metadata,
    Column('store_id', BigInteger, ForeignKey('stores.id'),
           nullable=False, index=True),
    Column('product_id', BigInteger, ForeignKey('products.id'),
           nullable=False, index=True),
    Column('quantity', Integer, nullable=False, default=0)
)

# class Stock(db.Model):
#     __tablename__ = 'stocks'
#     store_id = db.Column(db.BigInteger)
#     product_id = db.Column(db.BigInteger)
#     quantity = db.Column(db.Integer)

#     def __init__(self, store_id, product_id,
#                  quantity):
#         self.store_id = store_id
#         self.product_id = product_id
#         self.quantity = quantity

#     def __repr__(self):
#         return '<store: {}, product: {}> {}'.format(
#             self.store_id,
#             self.product_id,
#             self.quantity
#         )
