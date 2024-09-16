import sqlite3
DATABASE_PATH = './database/concerts.db'

def insert_test_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('ice', 'nashville')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('jamaica', 'kingston')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (5, 5, '2024-09-18')")

    
    conn.commit()
    conn.close()
    print("Test data inserted successfully.")



if __name__ == "__main__":
    insert_test_data()
   