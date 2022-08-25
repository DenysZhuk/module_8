from collections import defaultdict
from datetime import datetime
from typing import Dict, List


def get_weekday_by_id(weekday_id: int):
    weekday_map: Dict[int, str] = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    return weekday_map[weekday_id]


users_birthdays: List[Dict[str, datetime.date]] = [
    {"Alena": datetime(year=1988, month=6, day=12)},
    {"Denys": datetime(year=1985, month=7, day=1)},
    {"Oleksa": datetime(year=1994, month=6, day=4)},
    {"Nastya": datetime(year=1994, month=8, day=7)},
    {"Anna": datetime(year=1993, month=1, day=4)},
    {"Yulia": datetime(year=1992, month=2, day=26)},
    {"Ellina": datetime(year=1991, month=3, day=28)},
    {"Olga": datetime(year=1990, month=5, day=3)},
    {"Sarah": datetime(year=1998, month=7, day=19)},
    {"Michel": datetime(year=1999, month=8, day=20)},
    {"Misha": datetime(year=1998, month=9, day=1)},
]


def construct_current_date(day_of_birth: datetime.date):
    current_year = datetime.now().year
    return datetime(
        year=current_year, month=day_of_birth.month, day=day_of_birth.day
    ).date()


def get_birthdays_per_week(users: List[Dict[str, datetime]]):
    greeting_scheduler: Dict[str, List] = defaultdict(list)

    for user_dict in users:
        for username, birthday in user_dict.items():
            this_year_bd = construct_current_date(birthday)
            birthday_day_index = this_year_bd.weekday()
            weekday = get_weekday_by_id(birthday_day_index)
            if weekday in ["Sunday", "Saturday"]:
                weekday = "Monday"
            greeting_scheduler[weekday].append(username)
    print("\n")
    for weekday, birthday_guy in greeting_scheduler.items():
        print(f"{weekday}: " + ",".join(birthday_guy))
    return greeting_scheduler


if __name__ == "__main__":
    get_birthdays_per_week(users_birthdays)
