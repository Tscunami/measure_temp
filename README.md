# Measure temperature

## Description
This script is for my Raspberry Pi 4.  
I use SQLite db for storing information about temperature at given time.  
Script is scheduled to run every 10 minutes with Crontab

## Script called with Cron example
```bash
#!/bin/bash
cd /home/user/scripts/measure_temp
source venv/bin/activate
python run.py
deactivate
```

## Cronjob example
This will run every 10 minutes  
``*/10 * * * * ~/scripts/measure_temp/script.sh``  

## Additional scripts 

### motd.py
This script is called everytime, when any user ssh to Raspberry  
This script can be added to the folder **/etc/update-motd.d**  

#### Example file in /etc/update-motd.d
```shell
#!/bin/sh
cd /home/user/scripts/measure_temp
python motd.py
```
