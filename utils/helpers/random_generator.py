import random
import string
from datetime import datetime, timedelta


def generate_random_string(length):
    """
    Generates a random string of a specified length.

    Args:
        length (int): The desired length of the random string.

    Returns:
        str: A random string containing letters and digits.
    """
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

def generate_random_integer(first_num, last_num):
    """
    Generates a random integer within a specified range.

    Args:
        first_num (int): The start number (e.g., 1).
        last_num (int): The end number (e.g., 10).

    Returns:
        random_int: A random integer.
    """

    random_int = random.randint(first_num, last_num)  # Generates a random integer between 'first_num' and 'last_num'

    return random_int

def select_random_boolean():
    """
    Select random boolean between True/False.

    Returns:
        random_bool: True/False.
    """

    random_bool = random.choices([True, False])

    return random_bool

def generate_random_date_string(start_date_str, end_date_str):
    """
    Generates a random date string within a specified range.

    Args:
        start_date_str (str): The start date as a string (e.g., "2000-01-01").
        end_date_str (str): The end date as a string (e.g., "2025-12-31").

    Returns:
        str: A random date formatted as a string.
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    return f"{random_date.year}-{random_date.month}-{random_date.day}"
