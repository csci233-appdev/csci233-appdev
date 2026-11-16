import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')

    # Get a cursor.
    cur = conn.cursor()

    # Get product descriptions and retail prices.
    cur.execute('SELECT Description, RetailPrice FROM Products')

    # Fetch the results of the SELECT statement.
    results = cur.fetchall()

    # Iterate over the rows and display the results.
    for row in results:
        print(f'{row[0]:30} {row[1]:5}')

    # Close the database connection.
    conn.close()


# Execute the main function.
if __name__ == '__main__':
    main()
