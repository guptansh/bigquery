from google.cloud import storage
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r'C:\Users\anshu\PycharmProjects\CommonProject\gcp\basics-learning-282720-9cd0234ff159.json'
project_id = 'basics-learning-282720'

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))

upload_blob('craft_beer', r'C:\dataset\Craft Beers Dataset\beers.csv', 'beers.csv')
#upload_blob('craft_beer', r'C:\dataset\Craft Beers Dataset\breweries.csv', 'breweries.csv')
#gs://craft_beer/beers.csv
#gs://craft_beer/breweries.csv

#temp,location,clouds,pressure,rain,time_stamp,humidity,wind
#42.42,Back Bay,1.0,1012.14,0.1228,1545003901,0.77,11.25
#upload_blob('pycode-storage', r'C:\dataset\Uber & Lyft Cab prices\Cab-Weather Data\Cab-Weather Data\weather.txt', 'weather.txt')

#distance,cab_type,time_stamp,destination,source,price,surge_multiplier,id,product_id,name
#0.44,Lyft,1544952607890,North Station,Haymarket Square,5,1.0,424553bb-7174-41ea-aeb4-fe06d4f4b9d7,lyft_line,Shared
#upload_blob('pycode-storage', r'C:\dataset\Uber & Lyft Cab prices\Cab-Weather Data\Cab-Weather Data\cab_rides.txt', 'cab_rides.txt')