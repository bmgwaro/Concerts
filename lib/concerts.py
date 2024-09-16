DATABASE_PATH = './database/concerts.db'
import sqlite3

def get_concert_band(concert_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # SQL query to get the band associated with a concert
    cursor.execute("""
        SELECT bands.* 
        FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.id = ?
    """, (concert_id,))

    band = cursor.fetchone()
    conn.close()
    return band



def get_concert_venue(concert_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # SQL query to get the venue associated with a concert
    cursor.execute("""
        SELECT venues.* 
        FROM venues
        JOIN concerts ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
    """, (concert_id,))

    venue = cursor.fetchone()
    conn.close()
    return venue


if __name__ == "__main__":
    # Example concert ID to test
    concert_id = 1  # Adjust this based on your data

    # Get and print the band for the concert
    band = get_concert_band(concert_id)
    if band:
        print("Band for concert:", band)
    else:
        print(f"No band found for concert ID {concert_id}")

    # Get and print the venue for the concert
    venue = get_concert_venue(concert_id)
    if venue:
        print("Venue for concert:", venue)
    else:
        print(f"No venue found for concert ID {concert_id}")


def hometown_show(concert_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
    """, (concert_id,))

    band_hometown, venue_city = cursor.fetchone()
    conn.close()

    return band_hometown == venue_city


def concert_introduction(concert_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT bands.name, bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
    """, (concert_id,))

    band_name, band_hometown, venue_city = cursor.fetchone()
    conn.close()

    return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"



band = get_concert_band(1)  
print("Band for concert 1:", band)

print(hometown_show(1))  
print(concert_introduction(1))  
    