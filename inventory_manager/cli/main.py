import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.product import Product
from models.category import Category
from models.supplier import Supplier

def main_menu(session):
    while True:
        print("\n=== Inventory Manager ===")
        print("1. Add Product")
        print("2. List Products")
        print("3. Search Product by Name")
        print("4. Delete Product by ID")
        print("5. Quit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_product(session)
        elif choice == '2':
            list_products(session)
        elif choice == '3':
            search_product(session)
        elif choice == '4':
            delete_product(session)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def add_product(session):
    name = input("Product name: ").strip()
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))

   
    categories = session.query(Category).all()
    print("Categories:")
    for c in categories:
        print(f"{c.id}: {c.name}")
    cat_id = int(input("Choose category ID: "))

    # Show suppliers
    suppliers = session.query(Supplier).all()
    print("Suppliers:")
    for s in suppliers:
        print(f"{s.id}: {s.name}")
    sup_id = int(input("Choose supplier ID: "))

    product = Product(name=name, price=price, stock=stock, category_id=cat_id, supplier_id=sup_id)
    session.add(product)
    session.commit()
    print(f"Added product '{name}' successfully.")

def list_products(session):
    products = session.query(Product).all()
    print("\nID | Name           | Price   | Stock | Category      | Supplier")
    print("-"*65)
    for p in products:
        print(f"{p.id:<3}| {p.name:<14}| ${p.price:<7.2f}| {p.stock:<5}| {p.category.name:<13}| {p.supplier.name}")

def search_product(session):
    term = input("Enter product name to search: ").strip()
    results = session.query(Product).filter(Product.name.ilike(f"%{term}%")).all()
    if not results:
        print("No products found.")
        return
    print("\nSearch Results:")
    for p in results:
        print(f"{p.id}: {p.name} - ${p.price:.2f} - Stock: {p.stock}")

def delete_product(session):
    try:
        pid = int(input("Enter Product ID to delete: "))
        product = session.query(Product).filter(Product.id == pid).first()
        if product:
            confirm = input(f"Confirm delete '{product.name}'? (y/n): ").lower()
            if confirm == 'y':
                session.delete(product)
                session.commit()
                print("Product deleted.")
            else:
                print("Delete cancelled.")
        else:
            print("Product not found.")
    except ValueError:
        print("Invalid ID.")
