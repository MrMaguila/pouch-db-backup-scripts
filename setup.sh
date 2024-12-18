#!/bin/bash
export POETRY_PATH=/home/$USER/.local/bin/poetry

# setup a cron job for automatic backup
echo "
    #!/bin/bash
    set -e
    echo "Starting backup..."
    $POETRY_PATH -C $PWD run python $PWD/src/save_backups.py 2>&1
    echo "Terminated"
" > save-backups.sh

sudo chmod +x save-backups.sh

crontab -l > cronfile
echo "0 22 * * * bash $PWD/save-backups.sh > /tmp/backup-logs2.txt" >> cronfile
crontab cronfile
rm cronfile
