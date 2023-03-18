#!/usr/bin/python3
"""Deletes all State objects that contains an 'a' in their name
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
        session = Session()

        try:
            states_with_a = session.query(State).\
                    filter(State.name.like('%a%'))

            for state in states_with_a:
                session.delete(state)

            session.commit()

        except Exception as e:
            print(f"Error: {str(e)}")

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
            print(f"Error: {str(e)}")
