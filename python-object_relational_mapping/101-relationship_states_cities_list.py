#!/usr/bin/python3
"""
    Adds the State object "California" (row) with the City "San Francisco"
    to states table
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import Base, City
    from relationship_state import State

    av = sys.argv
    try:
        conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
        engine = create_engine(conn)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            for state in session.query(State).order_by(State.id).all():
                print("{}: {}".format(state.id, state.name))
                for city in state.cities:
                    print("\t{}: {}".format(city.id, city.name))

        except Exception as e:
            print("Error: {}".format(str(e)))

        finally:
            session.close()

    except IndexError:
        print(f"Usage: {av[0]} <username> <password> <database>")

    except Exception as e:
        try:
            msg_0 = str(e).split('\n')[0]
            msg = msg_0.split(" ", 1)[1].split(",")[1].strip()[1:-2]
            print("{}: {}".format(e.__class__.__name__, msg))

        except Exception:
            print("Error: {}".format(str(e)))
