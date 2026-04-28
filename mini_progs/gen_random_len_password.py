#Створити функціюб що генерує випадковий пароль довжини
import random
import string

def generate_password(password_length):
    allowed_characters = (
    string.ascii_letters 
    + string.digits
    + string.punctuation
    )
    
    password = ""
    for character in range(password_length):
        password += random.choice(allowed_characters)
        
    return password

print(generate_password(10))
print(generate_password(6))    
        
