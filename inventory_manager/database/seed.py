import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.category import Category
from models.supplier import Supplier
from models.product import Product

def seed_data(session):
    # Check if data already exists
    if session.query(Category).count() > 0:
        return

    # Add Categories
    cat_books = Category(name='Books')
    cat_electronics = Category(name='Electronics')
    session.add_all([cat_books, cat_electronics])

    # Add Suppliers
    sup_abc = Supplier(name='ABC Supplies', contact_info='abc@example.com')
    sup_xyz = Supplier(name='XYZ Traders', contact_info='xyz@example.com')
    session.add_all([sup_abc, sup_xyz])

    session.commit()

    # Add Products
    p1 = Product(name='Learn Python', price=29.99, stock=10, category=cat_books, supplier=sup_abc)
    p2 = Product(name='Laptop', price=999.99, stock=5, category=cat_electronics, supplier=sup_xyz)
    session.add_all([p1, p2])
    session.commit()
