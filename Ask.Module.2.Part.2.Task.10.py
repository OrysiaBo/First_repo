#def print_several_args(first_number, *args):
    #print(first_number)
    #print(args)
    #print(type(args)) 
    
    
#print_several_args(10, 100, 79, 20)

def print_several_args(first_number, *args, **kwargs):
    print(first_number)
    print(args)
    print(kwargs)
    
print_several_args(first_number=10, 
                   first_unexpekted_arg=100,
                   second_unexpekted_arg=78
                   )