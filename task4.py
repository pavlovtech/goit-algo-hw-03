from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Parse the birthday string into a date object, ignoring the year
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Adjust birthday to this year for comparison
        birthday_this_year = birthday_date.replace(year=today.year)

        # If the birthday has already occurred this year, consider the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference in days from today
        delta = (birthday_this_year - today).days

        if 0 <= delta <= 7:
            # If the birthday falls on a weekend, adjust to next Monday
            if birthday_this_year.weekday() >= 5:  # Saturday is 5, Sunday is 6
                days_to_add = 7 - birthday_this_year.weekday()
                birthday_this_year = birthday_this_year + timedelta(days=days_to_add)

            # Append the adjusted birthday to the list
            upcoming.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.04.26"},
    {"name": "Jane Smith", "birthday": "1990.04.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
