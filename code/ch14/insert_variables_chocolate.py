# Another example, insert into the chocolates Products table, so can use
# examples from 14.6 and 14.7 on selecting, updating and deleting the
# chocolate database
import sqlite3


def main():
    # Loop-control variable
    again = 'y'

    # Connect to the database.
    conn = sqlite3.connect('chocolate.db')

    # Get a cursor.
    cur = conn.cursor()
    while again == 'y':
        # Get the item name and price.
        description = input('Item Description: ')
        unit_cost = float(input('Unit Cost: '))
        retail_price = float(input('Retail Price: '))
        units_on_hand = int(input('Units on Hand: '))

        # Add the item to the Inventory table.
        cur.execute('''INSERT INTO Products (Description, UnitCost, RetailPrice, UnitsOnHand)
                       VALUES (?, ?, ?, ?)''',
                       (description, unit_cost, retail_price, units_on_hand))

        # Add another?
        again = input('Add another item? (y/n): ')

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# Execute the main function.
if __name__ == '__main__':
    main()