from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}
    today = datetime.now()
    names = {'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []}
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year+1)
        if today <= birthday_this_year <= today + timedelta(days=7):
            day_week = birthday_this_year.strftime("%A")
            if day_week in ("Saturday", "Sunday"):
                names["Monday"].append(name)
            else:
                names[day_week].append(name)
    return {key:value for key, value in names.items() if value}
    

names_users = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 8)},
               {"name": "Petr", "birthday": datetime(1945, 3, 9)},
               {"name": "Maria", "birthday": datetime(1955, 3, 4)},
               {"name": "Emil", "birthday": datetime(1975, 3, 7)}]
b_days = get_birthdays_per_week(names_users)
for day_week, names in b_days.items():
    print(f"{day_week}: {', '.join(names)}") 