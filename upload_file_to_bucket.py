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