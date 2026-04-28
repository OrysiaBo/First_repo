string = input()
# "apple,sun,man" -> ["apple", "sun", man]

strings_array = string.split(',');

match strings_array:
    case ["apple"]:
        print("only apple")
    case ["sun" | "earth", "man"]:
        print("sun of earth")
    
