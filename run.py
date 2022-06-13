"""Script for measuring temperature of Raspberry PI and save to sqlite db"""
import datetime
import os
import re

from sqlalchemy.orm import Session

from db import engine, meta_data


T_TEMPERATURES = meta_data.tables["temperatures"]


def get_temperature() -> str:
    """
    Gets current temperature and returns it as string
    :return: str, current temperature
    """

    full_temp = os.popen("vcgencmd measure_temp").read()

    # In format eg. 52.3
    formatted_temp = re.search(r"(\d*\.\d*)", full_temp).group(0)

    return formatted_temp


def add_temperature_to_db(temp: str) -> None:
    """Adds temperature to db"""

    current_time = datetime.datetime.now()

    with Session(engine) as session:
        session.execute(
            T_TEMPERATURES.insert().values(temperature=temp, created_at=current_time)
        )
        session.commit()


def main() -> None:
    """Executed on startup"""

    temperature = get_temperature()
    add_temperature_to_db(temperature)


if __name__ == "__main__":
    main()
