status = int(input())

if status == 200:
    print("ok")
elif status == 201:
    print("created")
elif status == 404:
    print("not found")
elif status == 500:
    print("internal erver error")
else:
    print("error")
    
match status:
    case 200:
        print("ok")
    case 201:
        print("created")
    case 404:
        print("not found")
    case 500:
        print("internal ever error")
else:
    print("error")
            
            