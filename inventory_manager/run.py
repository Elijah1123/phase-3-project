from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from database.seed import seed_data
from cli.main import main_menu

def main():
    engine = create_engine('sqlite:///inventory.db')
    Session = sessionmaker(bind=engine)
    session = Session()

   
    Base.metadata.create_all(engine)

    
    seed_data(session)

    
    main_menu(session)

if __name__ == '__main__':
    main()
