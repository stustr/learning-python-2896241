

def palindrome_test():
    user_input = input("Enter a string to test whether it is a palindrome or \"exit\": ")
    s = user_input.lower().strip()
    if s == "exit":
        return 0
    elif (user_input == user_input[::-1]):
        print("It is a palindrome")
    else:
        print("Nope not this one.")
    
    
 
palindrome_test()
