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
# name = input('Input your name: ')
# age = int(input('Input your age: '))
# print('Your name is ' + name + ' and you are', age)

# list 
states = ['Illinois', 'Florida', 'Colorado', 'New York', 'Arizona']
# replacing state with a different state
states[1] = 'Texas'
print(states)
# returns state (1)FLorida and the (3) letter r
print(states[1][3])
# gets every state after x number in this case (2) will get states CO, NY, AZ
print(states[2:])
# gets states from 1-3 FL and CO
print(states[1:3])
# lenght of list/array
print(len(states)) 
# joining 2 lists
list1 = ['Lexi', 'Millie', 'Andy']
list2 = [1, 2, 3, 4, 5]
# add to the end of list 1
list1.append('JP')
# will add to index 1
list1.insert(1, 'Nikki')
list1.extend(list2)
print(list1)

