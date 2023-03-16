#!/usr/bin/python3
""" This script list all states from the database `hbtn_0e_0_usa` """
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = None
    try:
        argv = sys.argv
        conn_dict = {
            'host': 'localhost',
            'port': 3306,
            'user': f'{argv[1]}',
            'passwd': f'{argv[2]}',
            'db': f'{argv[3]}'
        }

        conn = MySQLdb.connect(**conn_dict)
        cur = conn.cursor()

        try:
            query = "SELECT cities.name\
                     FROM cities\
                     INNER JOIN states ON cities.state_id = states.id\
                     WHERE states.name = %s;"

            cur.execute(query, (argv[4],))
            query_rows = cur.fetchall()
            output = ', '.join([t[0] for t in query_rows])
            print(output)

        except MySQLdb.Error as e:
            print(f"An error ocurred while excecuting the query: {e}")
        finally:
            cur.close()

    except Exception as e:
        print(f"An error ocurred while connecting to the database: {e}")

    finally:
        try:
            if conn:
                conn.close()
        except MySQLdb.Error as e:
            print(f"Error closing database connection: {e}")
