# WAP to find the sum of the digits of a number using UDF

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("The sum of digits is", result)