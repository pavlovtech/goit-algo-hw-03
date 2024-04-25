from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Convert the string date to a datetime object
        given_date = datetime.strptime(date_str, '%Y-%m-%d')
        # Get today's date with time stripped (only year, month, day)
        today_date = datetime.today().date()
        # Calculate the difference in days
        delta = today_date - given_date.date()
        # Return the difference in days
        return delta.days
    except ValueError as e:
        # If there is a format error or invalid date, raise an exception with a custom message
        raise ValueError("Incorrect date format or invalid date. Please use 'YYYY-MM-DD'.") from e

# Test
print(get_days_from_today("2021-10-09"))
