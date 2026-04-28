#В залежності від оцінки визначити коментар викладача до роботи 
# >= 90: excellent
#  75-89: well done
# 60-74: you can do better
# інша: You dont pass the exam

grade = int(input("Enter your grade: "))

if grade >= 90:
        print("Excellent!")  
elif grade >= 75:
        print("Well done!")
elif grade >= 60:
        print("You can so better!")
else:
        print("You dont pass the exam!")
        
print(grade)
