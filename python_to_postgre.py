import psycopg2

hostname = "localhost"
database = "Airbnb"
username = "postgres"
password = "8ENAjzSc*setUN"
port_id = "5433"
conn = None
cur = None

try: 
    conn = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port_id
    )
    print("Connected to the database successfully.")
    cur = conn.cursor()

    
    
    create_table_query = """ CREATE TABLE listings (
        id BIGINT PRIMARY KEY,
        listing_url TEXT NOT NULL,
        scrape_id BIGINT NOT NULL,
        last_scraped TIMESTAMP NOT NULL,
        name TEXT,
        description TEXT,
        neighborhood_overview TEXT,
        picture_url TEXT NOT NULL,
        host_id BIGINT NOT NULL,
        host_url TEXT NOT NULL,
        host_name TEXT,
        host_since DATE,
        host_location TEXT,
        host_about TEXT,
        host_response_time TEXT,
        host_response_rate FLOAT,
        host_acceptance_rate FLOAT,
        host_is_superhost BOOLEAN,
        host_thumbnail_url TEXT,
        host_picture_url TEXT,
        host_neighbourhood TEXT,
        host_listings_count FLOAT,
        host_total_listings_count FLOAT,
        host_verifications TEXT,
        host_has_profile_pic BOOLEAN,
        host_identity_verified BOOLEAN,
        neighbourhood TEXT,
        neighbourhood_cleansed TEXT NOT NULL,
        neighbourhood_group_cleansed FLOAT,
        latitude FLOAT NOT NULL,
        longitude FLOAT NOT NULL,
        property_type TEXT NOT NULL,
        room_type TEXT NOT NULL,
        accommodates INTEGER NOT NULL,
        bathrooms FLOAT,
        bathrooms_text TEXT,
        bedrooms FLOAT,
        beds FLOAT,
        amenities TEXT NOT NULL,
        price BIGINT NOT NULL,
        minimum_nights INTEGER NOT NULL,
        maximum_nights INTEGER NOT NULL,
        minimum_minimum_nights FLOAT,
        maximum_minimum_nights FLOAT,
        minimum_maximum_nights FLOAT,
        maximum_maximum_nights FLOAT,
        minimum_nights_avg_ntm FLOAT,
        maximum_nights_avg_ntm FLOAT,
        calendar_updated FLOAT,
        has_availability BOOLEAN,
        availability_30 INTEGER NOT NULL,
        availability_60 INTEGER NOT NULL,
        availability_90 INTEGER NOT NULL,
        availability_365 INTEGER NOT NULL,
        calendar_last_scraped TIMESTAMP NOT NULL,
        number_of_reviews INTEGER NOT NULL,
        number_of_reviews_ltm INTEGER NOT NULL,
        number_of_reviews_l30d INTEGER NOT NULL,
        first_review TIMESTAMP,
        last_review TIMESTAMP,
        review_scores_rating FLOAT,
        review_scores_accuracy FLOAT,
        review_scores_cleanliness FLOAT,
        review_scores_checkin FLOAT,
        review_scores_communication FLOAT,
        review_scores_location FLOAT,
        review_scores_value FLOAT,
        license TEXT,
        instant_bookable BOOLEAN,
        calculated_host_listings_count INTEGER NOT NULL,
        calculated_host_listings_count_entire_homes INTEGER NOT NULL,
        calculated_host_listings_count_private_rooms INTEGER NOT NULL,
        calculated_host_listings_count_shared_rooms INTEGER NOT NULL,
        reviews_per_month FLOAT
    );"""

    cur.execute(create_table_query)
    conn.commit()
except Exception as e:
    print("Error connecting to the database:", e)
    raise
finally:
    if cur is not None:
        cur.close()
        print("Cursor closed.")
    if conn is not None:
        conn.close()
        print("Connection closed.")