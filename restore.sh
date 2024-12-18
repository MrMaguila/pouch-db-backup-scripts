#!/bin/bash

export POUCH_DB_DATA_PATH=/var/lib/couchdb
export POUCH_DB_CONFIGS_PATH=/opt/couchdb/etc

sudo service couchdb stop;

if [[ -f /tmp/pouchdb/new/data-backup.zip ]] ; then
    echo "Restoring pouchdb data...";
    mv POUCH_DB_DATA_PATH /tmp/pouchdb/backup-trash/data;
    unzip /tmp/pouchdb/new/data-backup.zip -d $POUCH_DB_DATA_PATH.zip;
fi

if [[ -f configs-backup.zip ]] ; then
    echo "Restoring pouchdb configs...";
    mv POUCH_DB_CONFIGS_PATH /tmp/pouchdb/backup-trash/configs;
    unzip /tmp/pouchdb/new/configs-backup.zip -d $POUCH_DB_CONFIGS_PATH.zip;
fi

sudo systemctl restart couchdb