"""Script, which is called from script in /etc/update-motd.d"""

import datetime
import sqlite3
from typing import Tuple

from save_current_temp import get_temperature
from db_sqlite3 import connect_to_db


def get_max_temperature(cur: sqlite3.Cursor) -> Tuple[str, str]:
    """
    Find max temperature from today and returns its value and time
    :param cur: sqlite3.Cursor
    :return Tuple[str, str]
    """

    today = get_today_date()

    # Get max temperature from today
    try:
        cur.execute(f"SELECT MAX(temperature), created_at FROM temperatures WHERE created_at>'{today}';")
        temp, date = cur.fetchone()
        t_time = date.split(" ")[1]
        t_time = t_time.split(".")[0]
    except Exception:
        t_time, temp = "", "    "

    return temp, t_time


def get_min_temperature(cur: sqlite3.Cursor) -> Tuple[str, str]:
    """
    Find min temperature from today and returns its value and time
    :param cur: sqlite3.Cursor
    :return Tuple[str, str]
    """

    today = get_today_date()

    # Get min temperature from today
    try:
        cur.execute(f"SELECT MIN(temperature), created_at FROM temperatures WHERE created_at>'{today}';")
        temp, date = cur.fetchone()
        t_time = date.split(" ")[1]
        t_time = t_time.split(".")[0]
    except Exception:
        t_time, temp = "", "    "

    return temp, t_time


def get_today_date() -> str:
    """
    Gets today date at time 0:00:00.0
    :return str
    """

    today_datetime = datetime.datetime.now()
    today_datetime = today_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    return str(today_datetime)


def show_temperatures() -> None:
    """Prints today max, min and current temperatures with time"""

    # Connect to db
    connection, cursor = connect_to_db()

    # Get temperatures
    max_temp, max_time = get_max_temperature(cursor)
    min_temp, min_time = get_min_temperature(cursor)
    current_temperature = get_temperature()

    print("")
    print("Today temperatures:")
    print(30 * "-")
    print(f"Max: {max_temp}°C   Time: {max_time}")
    print(f"Min: {min_temp}°C   Time: {min_time}")
    print(f"Now: {current_temperature}°C")
    print("")


if __name__ == "__main__":
    show_temperatures()
