import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contact_info = Column(String)

    products = relationship('Product', back_populates='supplier')

    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}', contact='{self.contact_info}')>"
