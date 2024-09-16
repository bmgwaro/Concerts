DATABASE_PATH = './database/concerts.db'
import sqlite3

def get_band_concerts(band_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    
    cursor.execute("""
        SELECT * 
        FROM concerts
        WHERE band_id = ?
    """, (band_id,))

    concerts = cursor.fetchall()
    conn.close()
    return concerts


def get_band_venues(band_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    
    cursor.execute("""
        SELECT DISTINCT venues.* 
        FROM venues
        JOIN concerts ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
    """, (band_id,))

    venues = cursor.fetchall()
    conn.close()
    return venues


if __name__ == "__main__":
    
    band_id = 1  
    
    concert = get_band_concerts(band_id)
    if concert:
        print("concert for band:", concert)
    else:
        print(f"No concert found for band ID {band_id}")

    
    venue = get_band_venues(band_id)
    if venue:
        print("venue for band:", concert)
    else:
        print(f"No venue found for band ID {band_id}")


def play_in_venue(self, venue, date):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

   
    cursor.execute("""
        SELECT id FROM venues WHERE title = ?
    """, (venue,))
    venue_id = cursor.fetchone()

    if venue_id:
        cursor.execute("""
            INSERT INTO concerts (band_id, venue_id, date)
            VALUES (?, ?, ?)
        """, (self.id, venue_id[0], date))
        conn.commit()
        print(f"New concert added for band {self.name} at {venue} on {date}")
    else:
        print(f"Venue '{venue}' not found")

    conn.close()

def all_introductions(band_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        JOIN bands ON concerts.band_id = bands.id
        WHERE bands.id = ?
    """, (band_id,))

    introductions = cursor.fetchall()
    conn.close()

    return [f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
            for venue_city, band_name, band_hometown in introductions]


def all_introductions(band_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        JOIN bands ON concerts.band_id = bands.id
        WHERE bands.id = ?
    """, (band_id,))

    introductions = cursor.fetchall()
    conn.close()

    return [f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
            for venue_city, band_name, band_hometown in introductions]



def most_performances():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT bands.name, COUNT(concerts.id) AS concert_count
        FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1
    """)

    band = cursor.fetchone()
    conn.close()
    return band[0]  



venue = get_band_venues(1)  
print("venue for band 1:", venue)

print(play_in_venue(1, "Venue Title", "2024-09-15"))  # Example for band 1
print(all_introductions(1))  # Example for band 1
print(most_performances())  # Find band with most concerts