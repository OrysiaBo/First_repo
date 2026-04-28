#local
#nonlocal


def counter():
    state = 3
    
    def inner_func():
        nonlocal state 
        state = 5
        
    result = inner_func()
    return state
     
print(counter())
