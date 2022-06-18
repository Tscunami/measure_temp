"""Delete old entries from db"""

import datetime

from motd import connect_to_db


def delete_old_records() -> None:
    """Delete record from table which are older than defined"""

    # Connect to db
    connection, cursor = connect_to_db()

    # Get date 7 days back
    today_datetime = datetime.datetime.now()
    today_datetime = today_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    some_days_back = today_datetime - datetime.timedelta(days=3)
    time = str(some_days_back)

    # Delete all old records from db
    try:
        cursor.execute(f"DELETE FROM temperatures WHERE created_at<'{time}';")
        connection.commit()
    except Exception as err:
        print(f"Unable to delete old records from db: '{err}'")


if __name__ == "__main__":
    delete_old_records()

