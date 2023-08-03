#!/usr/bin/env python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>")
        return

    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create connection to MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given state name
    result = session.query(State).filter_by(name=state_name).first()

    # Check if a state with the given name was found
    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()

