#!/usr/bin/python3
"""Start link class to table in database
"""

if __name__ == "__main__":
    import re
    import sys
    from sqlalchemy import create_engine, inspect
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    av = sys.argv
    try:
        conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
        engine = create_engine(conn)

        inspector = inspect(engine)
        if not inspector.has_table("states"):
            Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        with Session() as session:
            for state in session.query(State).order_by(State.id).all():
                print("{}: {}".format(state.id, state.name))

    except IndexError:
        print("Usage: {} <username> <password> <database>".format(av[0]))
    except Exception as e:
        try:
            msg_0 = str(e).split('\n')[0]
            msg = msg_0.split(" ", 1)[1].split(",")[1].strip()[1:-2]
            print("Error: {}".format(msg))
        except Exception:
            print("Error: {}".format(str(e)))
