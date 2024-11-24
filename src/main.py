import sys
from datetime import date, strftime
from configs import PROJECT_ID, BUCKET_NAME, POUCH_DB_DATA_FOLDER, POUCH_DB_CONFIGS_FOLDER
from google.cloud import storage


if __name__ == "__main__":
    storage_client = storage.Client(project=PROJECT_ID)
    buckets = storage_client.list_buckets()
    
    bucket = None
    if BUCKET_NAME not in [bucket.name for bucket in buckets]:
        new_bucket = storage_client.bucket(BUCKET_NAME)
        new_bucket.storage_class = "COLDLINE"
        new_bucket.versioning_enabled = True
        #new_bucket.retention_period = 1000000
        new_bucket = storage_client.create_bucket(new_bucket)
        bucket = new_bucket
    else:
        bucket = storage_client.bucket(BUCKET_NAME)
        
    data_backup = bucket.blob("data-" + date.today().strftime("%d-%m-/%Y"))
    configs_backup = bucket.blob("configs-" + date.today().strftime("%d-%m-/%Y"))

    data_backup.upload_from_filename(POUCH_DB_DATA_FOLDER, if_generation_match=0)
    configs_backup.upload_from_filename(POUCH_DB_CONFIGS_FOLDER, if_generation_match=0)