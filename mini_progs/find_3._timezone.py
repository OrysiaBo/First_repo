#Виверження вулкану відбулось о 12:45:19 30.04.2020 за Гринвічем
#Вивести час у 3му часовому поясі
from datetime import datetime, timezone, timedelta
eruption_datetime = datetime(
    year=2020,
    month=4,
    day=30,
    hour=12,
    minute=45,
    second=19,
    tzinfo=timezone.utc,
)
third_timezone = timezone(timedelta(hours=3))
third_timezone_eruption_datetime = eruption_datetime.astimezone(third_timezone)
print(
    "Eruption datetime in 3 timezone: ",
    third_timezone_eruption_datetime.strftime("%d.%m.%y %H:%M:%S"),
    )

