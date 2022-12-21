from osm_requests import fetch_benches

print("Force syncing benches...")
fetch_benches.store_osm_benches()
print("Done!")