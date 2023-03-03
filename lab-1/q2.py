# WAP to check whether a number is positive or negative using user defined function

def check_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:       
        print("Negative")
    else:
        print("Zero")
        
number = int(input("Enter a number: "))
check_sign(number)