import os
from google.cloud import storage

# Configuration
# Set your bucket name here or via environment variable
BUCKET_NAME = os.environ.get("GCP_GCS_BUCKET", "zoomcamp_taxi_data")

def upload_to_gcs(bucket_name, object_name, local_file):
    """
    Uploads a local file to the bucket.
    """
    # Optimization for larger files
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024 
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024 

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    
    print(f"Uploading {local_file} to {object_name}...")
    blob.upload_from_filename(local_file)
    print(f"Success: {local_file} is now in {bucket_name}")

def upload_local_files_to_gcs():
    services = ['green', 'yellow']
    years = ['2019', '2020']

    for service in services:
        for year in years:
            for i in range(1, 13):
                month = f"{i:02d}"
                
                # Matching your local format: service_tripdata_YYYY-MM.csv.gz
                file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
                
                # Path in GCS (creates folders by service)
                gcs_path = f"{service}/{file_name}"

                if os.path.exists(file_name):
                    upload_to_gcs(BUCKET_NAME, gcs_path, file_name)
                else:
                    print(f"Skipping: {file_name} not found in current directory.")

if __name__ == "__main__":
    upload_local_files_to_gcs()