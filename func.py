def fnc(a, **b): 
    sum = a 
    for k in b: 
        sum += b[k] 
    return sum

result = fnc(10, k=1, n=2, i=3, m=4)
print(result)
