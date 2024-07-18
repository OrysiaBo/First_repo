#Визначити у який день тижня у вас буде день народження
#у 2025 роцію Дату увести у форматі "dd-mm"
import datetime

# Запитати у користувача дату народження у форматі "dd-mm"
datetime_string = input("Enter your birthday in 'dd-mm' format: ")

# Додати рік 2025 до дати народження
#full_datetime_string = datetime_string + "-2025"

# Перетворення на об'єкт datetime
#try:
    #birthday = datetime.datetime.strptime(full_datetime_string, "%d-%m-%Y")
    # Визначити день тижня
    #day_of_week = birthday.strftime("%A")  # "%A" використовується для отримання повної назви дня тижня
    # Вивести день тижня
    #print(f"Your birthday in 2025 will be on a {day_of_week}.")
#except ValueError as e:
    #print(f"Error: {e}. Please ensure you enter the date in 'dd-mm' format.")
    
birthday = datetime.datetime.strptime(
    datetime_string,
    "%d-%m"
)

b_2025 = birthday.replace(year=2025);

print(b_2025.strftime("%A"))
