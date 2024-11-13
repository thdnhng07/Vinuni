# # Functions and modules

# import shape
# shape_input = input()
# dimension = map(int, input().split())

# if shape_input == 'rectangle':
#     rectangle_area, rectangle_perimeter = shape.calculate_rectangle(*dimension)
#     print(f'Area: {rectangle_area}, Perimeter: {rectangle_perimeter}')

# elif shape_input == 'circle':
#     circle_area, circle_perimeter = shape.calculate_circle(*dimension)
#     print(f'Area: {circle_area}, Perimeter: {circle_perimeter}')

# elif shape_input == 'triangle':
#     triangle_area, triangle_perimeter = shape.calculate_triangle(*dimension)
#     print(f'Area: {triangle_area}, Perimeter: {triangle_perimeter}')


# # Debugging and testing

# def expression(a, b = 2.58):

#     assert a >= 0 and b >= 0, 'Only non-negative numbers must be provided'
#     try:
#         ex = (2 + a) / b

#     except ZeroDivisionError:
#         return -1
    
#     else:
#         return ex


# a, b = map(int, input().split())


# print(expression(a, b))



# # String manipulation

# def caesar_decrypt(message, shift):

#     decrypt_message = ''

#     for char in message:

#         if char.isalpha():

#             if char.islower(): 
#                 shift_base = ord('a')

#             else:
#                 shift_base = ord('A')

#             decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
#             decrypt_message += decrypted_char

#         else:
#             decrypt_message += decrypted_char

#     return decrypt_message


# message = input()
# shift = int(input())
# print(caesar_decrypt(message, shift))


# # List I

# drinks_list = [
#     "Green tea",
#     "Black tea",
#     "Oolong tea",
#     "White tea",
#     "Lemonade",
#     "Herbal tea",
#     "Milk tea",
#     "Bubble milk tea"
# ]


# def print_list():
#     print('/n'.join(drink_list))

# def find_drink():

#     keyword = input('Enter the keyword: ')
#     found_drinks = [drink for drink in drink_list if keyword.lower() in drink.lower()]
#     if found_drinks:
#         print('\n'.join(found_drinks))
#     else:
#         print('No drink found.')


# def add_drink():

#     drink_name = input('Enter the name of the drink: ')
#     drink_list.append(drink_name)
#     print(f'{drink_name} has been added to the list.')

# def remove_drink():

#     drink_name = input('Enter the name of the drink: ')
#     if drink_name in drink_list:
#         drink_list.remove(drink_name)
#         print(f'{drink_name} has been removed from the list.')
#     else:
#         print('No drink found.')


# prompt = int(input('''What do you want to do? 
# 1. Print the drink list
# 2. Find drink by keyword
# 3. Add a new drink to list
# 4. Delete a drink
# Please select a number (from 1-> 4):
# '''))



# if prompt == 1:
#     print_list()
# elif prompt == 2:
#     find_drink()
# elif prompt == 3:
#     add_drink()
# elif prompt == 4:
#     remove_drink()



# # List II

# molecules = list(map(int, input().split()))
# nuclear = []

# no_0 = molecules.count(0)


# for element in molecules[:]:
#     if element < 0:
#         molecules.remove(element) 
#     elif element > 0:
#         if element not in nuclear:
#             nuclear.append(element)

#     else:
#         continue

# print(molecules)
# print(nuclear)


# print(nuclear)
    
# for i in range(no_0):
#     nuclear.append(0)

# print(*nuclear)

x = 1
print(lambda x: x + 1)


