#!/usr/bin/python3
"""Prints all City objects
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    av = sys.argv
    try:
        conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
        engine = create_engine(conn)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            for columns in session.query(State.name, City.id, City.name).\
                    join(State).\
                    order_by(City.id):
                print("{}: ({}) {}".format(columns[0], columns[1], columns[2]))

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            session.close()

    except IndexError:
        print("Usage: {} <username> <password> <database>".format(av[0]))

    except Exception as e:
        try:
            msg_0 = str(e).split('\n')[0]
            msg = msg_0.split(" ", 1)[1].split(",")[1].strip()[1:-2]
            print("{}: {}".format(e.__class__.__name__, msg))
        except Exception:
            print("Error: {}".format(str(e)))
