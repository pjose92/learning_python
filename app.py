# greetings = 'hello there!'
# age = 30
# first_name = 'JP'
# last_name = 'Perez'
# print(greetings.upper()) 
# print(greetings.islower()) 
# print(len(greetings))
# print(age)
# print(first_name)
# print(last_name)

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(3, 5)
# print("The sum is:", result)
# print(max(3, 4, 18, 2, 5, 19))
# print(min(3, 4, 18, 1, 30, 20))

# # User's input
# # name = input('Input your name: ')
# # age = int(input('Input your age: '))
# # print('Your name is ' + name + ' and you are', age)

# # list 
# states = ['Illinois', 'Florida', 'Colorado', 'New York', 'Arizona']
# # replacing state with a different state
# states[1] = 'Texas'
# print(states)
# # returns state (1)FLorida and the (3) letter r
# print(states[1][3])
# # gets every state after x number in this case (2) will get states CO, NY, AZ
# print(states[2:])
# # gets states from 1-3 FL and CO
# print(states[1:3])
# # lenght of list/array
# print(len(states)) 
# # joining 2 lists
# list1 = ['Lexi', 'Millie', 'Andy']
# list2 = [1, 2, 3, 4, 5]
# # add to the end of list 1
# list1.append('JP')
# # will add to index 1
# list1.insert(1, 'Nikki')
# list1.extend(list2)
# print(list1)

def find_largest_number(numbers):
    # Initialize the first number as the largest
    largest = numbers[0]
    
    # Loop through the list to find the largest number
    for number in numbers:
        if number > largest:
            largest = number
    
    return largest

# Example usage:
numbers = [3, 7, 1, 23, 14, 50, 2, 4, 100, 20, 10, 6, 1, 2, 3,0, 200]
largest_number = find_largest_number(numbers)
print(f"The largest number is: {largest_number}")



def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


def authenticate(username, password):
    """Simple authentication function."""
    valid_username = "admin"
    valid_password = "password123"
    
    if username == valid_username and password == valid_password:
        return "Authentication successful!"
    else:
        return "Authentication failed."

# Test the function
user = input("Enter username: ")
pwd = input("Enter password: ")
print(authenticate(user, pwd))


from cgi import print_environ
import random
import string

def generate_password(length=8):
    """Generate a random password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Test the function
length = int(input("Enter the desired password length: "))
print(f"Generated password: {generate_password(length)}")


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Test the function
terms = int(input("Enter the number of terms: "))
print(f"The first {terms} terms of the Fibonacci sequence are: {fibonacci(terms)}")
# moonxmgl

# topples - can't change it. it does allow repetition of same value 
three_numbers = tuple((1, 2, 3, 1, 2));
strings = ('home', 'land', 'eartch')
print(three_numbers)
print(len(three_numbers))
print(strings)
numbers_strings = (1, 2, 3, True, 'Home', 3, 1)
print(type(numbers_strings[0]))


