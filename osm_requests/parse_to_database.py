import pymysql
import json
import config

def parse_to_database():
    conn = open_connection()

    # Check if connection was successful
    if conn.open:
        print("Succesfully connected to database!")

    # Create cursor
    cur = conn.cursor()

    # Check if benches table exists
    cur.execute("SHOW TABLES LIKE 'benches'")
    result = cur.fetchone()
    if result:
        print("Table benches already exists")
    else:
        # Create benches table
        cur.execute("""
          CREATE TABLE `benches` (
            `id` BIGINT NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(255) DEFAULT NULL COMMENT 'name generated on request',
            `coordinates` POINT NOT NULL,
            `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            `deleted_at` TIMESTAMP NULL DEFAULT NULL,
            SPATIAL INDEX `SPATIAL` (`coordinates`),
            PRIMARY KEY (`id`)
          )
        """)
        print("Table benches created")

    # Close connection
    conn.close()

    # Load data from OSM benches.json file
    print("Loading data from OSM benches.json file...")
    with open('./data/benches.json') as json_file:
        data = json.load(json_file)

        print("File loaded, inserting data into database...")

        conn = open_connection()
        cur = conn.cursor()

        for bench in data['elements']:
          # Check if required fields are present
          if 'id' in bench and 'lat' in bench and 'lon' in bench:
            # Check if bench already exists
            cur.execute("SELECT * FROM benches WHERE id = %s", (bench['id']))
            result = cur.fetchone()
            if result:
              continue

            # Insert data into database
            cur.execute("""
              INSERT INTO benches (id, coordinates) VALUES (%s, POINT(%s, %s))
            """, (bench['id'], bench['lon'], bench['lat']))
            print("Bench with id " + str(bench['id']) + " inserted")

        # Commit changes
        print("Committing changes...")
        conn.commit()

        # Close connection
        conn.close()

def open_connection():
    return pymysql.connect(host=config.mysql_host, port=config.mysql_port, user=config.mysql_user, passwd=config.mysql_pass, db=config.mysql_database)