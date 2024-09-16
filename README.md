# Concert Domain Code Challenge

## Project Description
In this assignment, we are working with a **Concert Domain**. The project involves creating a relational database that models the relationships between **Bands**, **Venues**, and **Concerts**. A **Band** can have many concerts, a **Venue** can host many concerts, and a **Concert** belongs to both a band and a venue, establishing a many-to-many relationship between Bands and Venues.

Using raw SQL queries within Python, we will interact with this database to perform various operations like retrieving data, inserting records, and performing aggregate queries. We will not be using an ORM like SQLAlchemy for this project, but instead writing SQL queries directly within Python methods to manipulate and query the database.

## Technologies Used:
- Python
- SQLite3
- SQL
- SQLite


## Getting Started

1.  Click on [this link](https://github.com/bmgwaro/Concerts) in order to access the github repository containing this project.

2.  Click on fork to create copy of the repository.

3.  Open your terminal and navigate into the directory where you would like to save the work using the `cd` command.

        cd <directory_name>

4.  Copy and paste the following command in order to clone the repository into your local storage. Remember to replace `your_github_username` with your actual username.

        git clone git@github.com:your_github_username/Concerts.git

5.  Navigate into the newly cloned folder and type in the `code .` command in order to open it on your text editor.


## Database Schema

The project consists of the following tables:

- **bands**: Stores band details such as `id`, `name`, and `hometown`.
- **venues**: Stores venue details such as `id`, `title`, and `city`.
- **concerts**: Stores concert details such as `id`, `band_id`, `venue_id`, and `date`, and serves as a join table for the many-to-many relationship between bands and venues.

## Functionality

### Core Features:

#### Retrieve Band Information:
- **`get_concert_band(concert_id)`** - Retrieves the band associated with a specific concert.

#### Retrieve Venue Information:
- **`get_concert_venue(concert_id)`** - Retrieves the venue where a specific concert is held.

#### Check for Hometown Shows:
- **`hometown_show(concert_id)`** - Checks whether a band is performing in its hometown at a particular concert.

#### Generate Concert Introductions:
- **`concert_introduction(concert_id)`** - Returns a string introducing the band at a concert based on the band’s name, hometown, and the venue city.

#### Retrieve Concerts at a Venue:
- **`get_venue_concerts(venue_id)`** - Retrieves all concerts scheduled at a specific venue.

#### Retrieve Bands Performing at a Venue:
- **`get_venue_bands(venue_id)`** - Retrieves all the bands that have performed or will perform at a particular venue.

#### Retrieve Concert by Date:
- **`concert_on(venue_id, concert_date)`** - Checks if there is a concert at a specific venue on a given date.

#### Identify Most Frequent Band at a Venue:
- **`most_frequent_band(venue_id)`** - Returns the name of the band that has performed the most concerts at a specific venue.

#### Insert New Concert Data:
- **`play_in_venue(band_id, venue, date)`** - Schedules a new concert for a band at a specific venue on a given date.

#### Insert Test Data:
- **`insert_test_data()`** - Inserts sample data into the database to test the functionalities.

#### List All Venues for a Band:
- **`get_band_venues(band_id)`** - Lists all the venues where a band has performed.

#### List Concert Introductions:
- **`all_introductions(band_id)`** - Returns a list of formatted concert introductions for a specific band.

#### Most Performances:
- **`most_performances()`** - Finds the band that has performed the most concerts overall.
