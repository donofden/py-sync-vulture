# py-sync-vulture
A python script for syncing two folders in a machine.

![Py-Sync-Vulture](py-sync-vulture.png)

## Py-Sync-Vulture

The python script to synchronize files between local to another location in same machine.

The script `sync.py` used to synchronize files between locals in the same machine.

# How to use it:

- Update `Makefile` with the `SOURCE` & `DESTINATION` folders. The path should be from root.
- Run `make install-python-deps` to install python Dependencies for this project.
- To start sync `make sync` this will start synn between source and destination.

Note: If you want this sync to do **bidirectional** please check the following instructions.

- The sync can also be run with this command `python3 sync.py -src='SOURCE_PATH' -dest='DESTINATION_PATH`
- So to make is work for bidirectional run the above command twice one with 

`SOURCE_PATH`->`DESTINATION_PATH` 
& 
`DESTINATION_PATH`->`SOURCE_PATH`

# CRONTAB

If you to run this in CRON, created a crontab file called `/Users/aravindkumar/etc/crontab`, that looks like this:

`*/5 * * * * ~/FILE_STORED_PATH/sync.py -src='SOURCE_PATH' -dest='DESTINATION_PATH >/dev/null 2>&1`

Then I ran this crontab command to install the job:

`crontab /Users/aravindkumar/etc/crontab`

Files now auto-sync to /Volumes/Shared every 5 minutes. When there are no files to sync, the script completes in a couple seconds.

# Future Goal:

- Sync between two location inside a network of systems