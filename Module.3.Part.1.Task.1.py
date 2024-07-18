#Вирахувати чийсь вік
import datetime
import math

def calculate_age(year_of_birth: int) -> int:
    """
    calculate persone age based on birth yaer.
    """
    current_date: datetime.datetime = datetime.datetime.now()
    return math.floor(
        (current_date - birth_datetime).days/365.25
    )
    
def get_int_input(error_messege: str) -> int:
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print(error_messege)
    
birth_year = get_int_input("Please enter a valid year.")
birth_month = get_int_input("Please enter a valid month.")
birth_day = get_int_input("Please enter a valid day.")
birth_datetime = datetime.datetime(
    year=birth_year,
    month=birth_month,
    day=birth_day
)

print(calculate_age(birth_datetime))