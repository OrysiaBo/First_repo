state = 90

def counter():
    global state
    state += 3
    
    def inner_func():
        state = 5
        
    result = inner_func()
    return state
       
print(counter())
print(state)
