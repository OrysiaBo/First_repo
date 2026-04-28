#numbers = [10, 20, 30, 40]
#numbers2 = [1, 2, 3, 4]

#numbers_sum = 0
#for number in numbers:
    #numbers_sum += number

#numbers_sum2 = 0
#for number in numbers2:
    #numbers_sum2 += number
    
#print(numbers_sum)

#import pdb

#pdb.set_trace()


#def sum_numbers(sum_list):
    #numbers_sum = 0
    #for number in sum_list:
        #numbers_sum += number
    #return numbers_sum
    
#print(sum_numbers(numbers)) 
#print(sum_numbers(numbers, numbers2))   


numbers = [10, 20, 30, 40]
numbers2 = [1, 2, 3, 4]

def sum_numbers(sum_list):
    numbers_sum = 0
    for number in sum_list:
        numbers_sum += number
    return numbers_sum  # Додано повернення значення

print(sum_numbers(numbers))  # Викликаємо функцію з одним аргументом

print(sum_numbers(numbers2 + numbers))
