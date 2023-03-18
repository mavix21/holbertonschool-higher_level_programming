#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    av = sys.argv
    try:
        conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
        engine = create_engine(conn)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        with Session() as session:
            first_state = session.query(State).first()
            if first_state:
                print("{}: {}".format(first_state.id, first_state.name))
            else:
                print("Nothing")

    except IndexError:
        print("Usage: {} <username> <password> <database>".format(av[0]))
    except Exception as e:
        try:
            msg_0 = str(e).split('\n')[0]
            msg = msg_0.split(" ", 1)[1].split(",")[1].strip()[1:-2]
            print("Error: {}".format(msg))
        except Exception:
            print("Error: {}".format(str(e)))
