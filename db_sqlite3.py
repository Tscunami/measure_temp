"""Utils and connection for sqlite3"""

import sys
import sqlite3
from typing import Tuple

DB_NAME = "temperatures.db"


def connect_to_db() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Connect to db and returns its connection and cursor
    :return Tuple[sqlite3.Connection, sqlite3.Cursor]
    """

    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
    except Exception:
        print("Unable to connect to db for temperature.")
        sys.exit(0)

    return con, cur

