"""Script, which is called from script in /etc/update-motd.d"""

import datetime
import sqlite3

if __name__ == "__main__":

    today = str(datetime.datetime.now())

    # connect to db
    con = sqlite3.connect("temperatures.db")
    cur = con.cursor()

    # get min, max temp from today
    try:
        cur.execute("select max(temperature), created_at from temperatures;")
        max_temp, max_date = cur.fetchone()
        max_time = max_date.split(" ")[1]
        max_time = max_time.split(".")[0]
    except Exception as err:
        max_time, max_temp = "", "    "

    try:
        cur.execute("select min(temperature), created_at from temperatures;")
        min_temp, min_date = cur.fetchone()
        min_time = min_date.split(" ")[1]
        min_time = min_time.split(".")[0]
    except Exception as err:
        min_time, min_temp = "", "    "

    print(30 * "-")
    print("Today:")
    print(f"Max: {max_temp}°C   Time: {max_time}")
    print(f"Min: {min_temp}°C   Time: {min_time}")
    print(30 * "-")
