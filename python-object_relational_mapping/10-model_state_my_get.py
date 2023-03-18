#!/usr/bin/python3
"""Prints the State object with the name passed as argument
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    av = sys.argv
    try:
        conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
        searched = av[4]
        engine = create_engine(conn)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            states = session.query(State).filter(State.name == searched)

            if states.count() == 0:
                print("Not found")
            else:
                for state in states:
                    print(state.id)

        except Exception as e:
            print("Error: {}".format(str(e)))

        finally:
            session.close()

    except IndexError:
        print(f"Usage: {av[0]} <username> <password> <database> <state name>")

    except Exception as e:
        try:
            msg_0 = str(e).split('\n')[0]
            msg = msg_0.split(" ", 1)[1].split(",")[1].strip()[1:-2]
            print("{}: {}".format(e.__class__.__name__, msg))

        except Exception:
            print("Error: {}".format(str(e)))
