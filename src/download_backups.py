import sys
import os
from datetime import date
from shutil import make_archive

from configs import PROJECT_ID, BUCKET_NAME

from google.cloud import storage

def download_backups():
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.get_bucket(BUCKET_NAME)
    
    if bucket is None:
        print("Cannot download backup: bucket not found.")
        return
    
    data_backup = bucket.get_blob("data-backup.zip")
    configs_backup = bucket.get_blob("configs-backup.zip")
    
    if not data_backup.exists() or not configs_backup.exists():
        print("Cannot find configs backup file." if data_backup.exists() is not None else "Cannot find data backup file.")
        return
    
    data_backup.download_to_filename("/tmp/pouchdb/new/data-backup.zip")
    configs_backup.download_to_filename("/tmp/pouchdb/new/configs-backup.zip")

if __name__ == "__main__":
    download_backups()
