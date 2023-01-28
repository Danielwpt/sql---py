import sqlite3

try:
    test_conn = sqlite3.connect("test.db")

    #insert_query = "INSERT INTO People(name, age, address) VALUES ('Adam',12,'Sam 12');"

    test_cur = test_conn.cursor()

    print("Connected SQLite")

    select_query = "SELECT * FROM People;"
    test_cur.execute(select_query)

    #test_conn.commit()
    fetch_row = test_cur.fetchall()
    
    for rows in fetch_row:
        print(rows)
        
finally:
    test_cur.close()