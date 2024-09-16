DATABASE_PATH = './database/concerts.db'
import sqlite3

def get_venue_concerts(venue_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # SQL query to get all concerts at a venue
    cursor.execute("""
        SELECT * 
        FROM concerts
        WHERE venue_id = ?
    """, (venue_id,))

    concerts = cursor.fetchall()
    conn.close()
    return concerts


def get_venue_bands(venue_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # SQL query to get all bands that performed at a venue
    cursor.execute("""
        SELECT DISTINCT bands.* 
        FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
    """, (venue_id,))

    bands = cursor.fetchall()
    conn.close()
    return bands


if __name__ == "__main__":
    
    venue_id = 1  
    
    band = get_venue_bands(venue_id)
    if band:
        print("Band for venue:", band)
    else:
        print(f"No band found for venue ID {venue_id}")

    
    concert = get_venue_concerts(venue_id)
    if concert:
        print("concert for venue:", concert)
    else:
        print(f"No concert found for venue ID {venue_id}")



def concert_on(venue_id, concert_date):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * 
        FROM concerts 
        WHERE venue_id = ? AND date = ?
        LIMIT 1
    """, (venue_id, concert_date))

    concert = cursor.fetchone()
    conn.close()
    return concert  # Return the concert details


def most_frequent_band(venue_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT bands.name, COUNT(concerts.id) AS performance_count
        FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
    """, (venue_id,))

    band = cursor.fetchone()
    conn.close()
    return band[0]  # Return the name of the most frequent band


band = get_venue_bands(1)  
print("Band for venue 1:", band)

print(concert_on(1, "2024-09-15"))  # Example for venue 1 and date
print(most_frequent_band(1))  # Example for venue 1