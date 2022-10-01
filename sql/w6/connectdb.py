import psycopg2


def conn(db, user, password, host):
    con = psycopg2.connect(database=db, user=user, password=password, host=host)
    cur = con.cursor('c1')
    # cur.execute("""
    # select %s from res
    # """,
    # ['*'])
    cur.execute('select * from car')
    cur.itersize = 2
    for record in cur:
        print(record)

    con.close()



if __name__ == '__main__':

    db = 'cars'
    user = 'postgres'
    password = 'sql'
    host = 'localhost'

    conn(db, user, password, host)
