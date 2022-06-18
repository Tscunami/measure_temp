# Measure temperature

## Description
These scripts are for monitoring temperature on my Raspberry Pi 4.
I use SQLite db for storing information about temperature and current time.  

## Information before setting up
I installed sqlalchemy in my root python and use it across all projects.
If you want to install sqlalchemy in your venv, remove platform condition in requirements.txt.  
Next thing, if you don't have already, is to install sqlite3 on your system with:  
```sudo apt install sqlite3```

## Description of individual scripts

### save_current_temp.py
This script is for storing current temperature at given time.  
I scheduled it to run every 10 minutes with crontab.
Example script called with crontab:  
```bash
#!/bin/bash
cd /home/user/scripts/measure_temp
source venv/bin/activate
python save_current_temp.py
deactivate
```
Cronjob example:   
``*/10 * * * * ~/scripts/cron_scripts/save_current_temp.sh``  

### del_old_temps.py
This script is for deleting old data from db.  
Currently, it is set up to delete all records older than 3 days.  
Example script called with crontab:
```bash
#!/bin/bash
cd /home/user/scripts/measure_temp
python measure_temp
```
Cronjob example:   
``55 23 * * * ~/scripts/cron_scripts/del_current_temp.sh``  

### motd.py
This script is called everytime, when any user ssh to Raspberry.  
In order to run it, you have to add new script to **/etc/update-motd.d** directory.  
Example script in /etc/update-motd.d
```shell
#!/bin/sh
cd /home/user/scripts/measure_temp
python motd.py
```
