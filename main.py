from time import sleep
import schedule
from osm_requests import fetch_benches

print("Starting script...")

schedule.every().day.at("00:00").do(fetch_benches.store_osm_benches)

# Keep the script running
while True:
    schedule.run_pending()
    sleep(1)
