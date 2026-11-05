import sqlite3


def main():
    conn = sqlite3.connect('contacts.db')
    cur = conn.cursor()

    # Insert code here to perform operations on the database.

    conn.commit()
    conn.close()


# Execute the main function.
if __name__ == '__main__':
    main()
