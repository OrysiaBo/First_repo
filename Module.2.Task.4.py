#Зясувати чи є студент переможцем

winners_list = [
    "Alice Johnson",
    "Suasan Lingrett",
    "Stefen Lourens",
    "Orysia Bohachevska",
    "Jesus Christ",
    "Michael Jackson",
]

student_name = input("Input student name ")

#is_winner = (
    #"Student is winner"
    #if student_name is winners_list
    #else "Student is not winner"
#)

print(
    "Student is winner"
    if student_name in winners_list
    else "Student is not winner"
)

print(245)