# Another example, create the chocolate Products table, so can use
# examples from 14.6 and 14.7 on selecting, updating and deleting the
# chocolate database
import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')

    # Get a cursor.
    cur = conn.cursor()

    # Add the Inventory table.
    cur.execute('''CREATE TABLE Products (ProductID INTEGER PRIMARY KEY NOT NULL,
                                          Description TEXT,
                                          UnitCost REAL,
                                          RetailPrice REAL,
                                          UnitsOnHand INTEGER)''')

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# Execute the main function.
if __name__ == '__main__':
    main()
