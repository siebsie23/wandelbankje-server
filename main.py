from time import sleep
import schedule
from osm_requests import fetch_benches, parse_to_database

print("Starting script...")

sleep(10)
print('Connecting to database...')
parse_to_database.parse_to_database('hallo')

schedule.every().day.at("00:00").do(fetch_benches.store_osm_benches)

# Keep the script running
while True:
    schedule.run_pending()
    sleep(1)
