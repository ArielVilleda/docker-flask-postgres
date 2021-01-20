from sqlalchemy.orm import relationship
from sqlalchemy import (Column, ForeignKey,
                        BigInteger, String)

from app.main import db


class Product(db.Model):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True)
    name = Column(String())
    image = Column(String())
    stores = relationship(
        'Stock',
        back_populates='product'
    )

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __repr__(self):
        return '<id {}> {}'.format(self.id, self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    @staticmethod
    def all(**kwargs):
        query = Product.query
        return query.all()
