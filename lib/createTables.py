import sqlite3


DATABASE_PATH = '../database/concerts.db'
MIGRATION_FILE = '../migrations/createTables.sql'


def create_tables():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    
    with open(MIGRATION_FILE, 'r') as sql_file:
        sql_script = sql_file.read()

    
    cursor.executescript(sql_script)

    
    conn.commit()
    conn.close()
    print("Tables created successfully.")


if __name__ == "__main__":
    create_tables()
