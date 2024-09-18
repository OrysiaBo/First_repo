# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."

# Функція для отримання телефону за ім'ям
@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

# Функція для виведення всіх контактів
@input_error
def show_all(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "No contacts found."

# Основна функція для обробки команд
def main():
    contacts = {}
    
    commands = {
        "add": add_contact,
        "phone": get_phone,
        "all": lambda args, contacts: show_all(contacts),
    }

    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        
        command_args = input("Enter the argument for the command: ").strip().split()
        
        if command in commands:
            func = commands[command]
            result = func(command_args, contacts)
            print(result)
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
