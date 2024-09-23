greetings = 'hello there!'
age = 30
first_name = 'JP'
last_name = 'Perez'
print(greetings.upper()) 
print(greetings.islower()) 
print(len(greetings))
print(age)
print(first_name)
print(last_name)

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("The sum is:", result)
print(max(3, 4, 18, 2, 5, 19))
print(min(3, 4, 18, 1, 30, 20))

# User's input
name = input('Input your name: ')
age = int(input('Input your age: '))
print('Your name is ' + name + ' and you are', age)