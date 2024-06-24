#За допомогою тернарного оператора визначити чи учень склав екзамен (отримав від 60 балів)

grade = int(input("Enter grade: "))

#if grade >= 60:
    #passed_exam = "Passed"
#else:
    #passed_exam = "Not passed!"

passed_exam = "Passed" if grade >= 60 else "Not passed!"
print(passed_exam)