# Calculates the factorial of the given integer
def getting_factorial(number):
    if (number in range(0,2)):
        return 1
    else:
        return number * getting_factorial(number - 1)

# Gets the integer from the user
input_value = int(input("Enter a number to Find Factorial: "))

# Checks whether the integer is negative
if (input_value < 0):
    print("You should enter a non-negative integer!")
else:
    print(input_value,"! = ", getting_factorial(input_value))