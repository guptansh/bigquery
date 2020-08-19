from google.cloud import storage
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r'C:\Users\anshu\PycharmProjects\CommonProject\gcp\basics-learning-282720-9cd0234ff159.json'
project_id = 'basics-learning-282720'

def create_bucket(bucket_name):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket {} created".format(bucket.name))

create_bucket('craft_beer')