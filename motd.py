"""Script, which is called from script in /etc/update-motd.d"""

import datetime
import sqlite3
import sys

from run import get_temperature

if __name__ == "__main__":

    # Get today's datetime at 0:00:00
    today_datetime = datetime.datetime.now()
    today_datetime = today_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    today = str(today_datetime)

    # connect to db
    try:
        con = sqlite3.connect("temperatures.db")
        cur = con.cursor()
    except Exception as err:
        print("Unable to connect to db for temperature.")
        sys.exit(0)

    # Get max temperature from today
    try:
        cur.execute(f"select max(temperature), created_at from temperatures where created_at>'{today}';")
        max_temp, max_date = cur.fetchone()
        max_time = max_date.split(" ")[1]
        max_time = max_time.split(".")[0]
    except Exception as err:
        max_time, max_temp = "", "    "

    # Get min temperature from today
    try:
        cur.execute(f"select min(temperature), created_at from temperatures where created_at>'{today}';")
        min_temp, min_date = cur.fetchone()
        min_time = min_date.split(" ")[1]
        min_time = min_time.split(".")[0]
    except Exception as err:
        min_time, min_temp = "", "    "

    # Get current temperature
    current_temperature = get_temperature()

    print(30 * "-")
    print("Today:")
    print(f"Max: {max_temp}°C   Time: {max_time}")
    print(f"Min: {min_temp}°C   Time: {min_time}")
    print(f"Now: {current_temperature}°C")
    print(30 * "-")
