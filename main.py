# # Get input value
# inp_temp = float(input())
# inp_u = input()
# # Assign value in inp_u is blank
# if inp_u == '':
#     inp_u = "C"
# elif inp_u != '':
#     pass
# def convert_temperature(value: float, unit = 'C'):

#     # Convert from Celsius to Fahreheit
#     if unit == 'F':
#         Celsius = (value - 32) * 5/9
#         return Celsius
#     elif unit == 'C':
#     # Convert from Fahreheit to Celsius
#         Fahreheit = (value * 9/5) + 32
#         return Fahreheit
# # Print result
# # result = convert_temperature(inp_temp, inp_u)


# result = map(convert_temperature, inp_temp, )
# print('%.2f' % result)









# import random
# print (x:=random.randint(1, 100))





# print(ord('a'))
# print(ord('h'))

# string = input()
# subtring = input()

# for substring in range(0,len(string)):
#     print(string[substring])
# n1 = [1,2]
# n2 = [3,4]
# n1.append(n2)
# n2.append(n1)
# print(n1)
# new = n1 + n2
# print(len(new))


molecules = list(map(int, input().split()))
nuclear = []

no_0 = molecules.count(0)


for element in molecules[:]:
    if element < 0:
        molecules.remove(element) 
    elif element > 0:
        print(molecules.index(element))
        if element not in nuclear:
            nuclear.append(element)

    else:
        continue

    
for i in range(no_0):
    nuclear.append(0)

print(*nuclear)

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
#     found_drinks = [drink for drink in drinks_list if keyword.lower() in drink.lower()]
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
#     if drink_name in drinks_list:
#         drinks_list.remove(drink_name)
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















# # import math
# # # Get Xa, Ya, Xb, Yb
# # inp_a = input()
# # inp_b = input()
# # x_a, y_a = inp_a.split()
# # x_b, y_b = inp_b.split()
# # # Calculate dist
# # def calculate_disttance():
# #     """
# #     Calculate the Euclidean distance between two points in a 2D plane.
# #     This function calculates the distance between two points (Xa, Ya) and (Xb, Yb)
# #     using the Euclidean distance formula:
# #     distance = sqrt((Xb - Xa)² + (Yb - Ya)²)
# #     The calculation is done in two steps:
# #     1. The square of the differences in the x and y coordinates is computed.
# #     2. The sum of these squared differences is used to calculate the distance.
# #     Returns:
# #     float: The Euclidean distance between the two points, rounded to two decimal
# #     places.
# #     """
# #     def square_difference():
# #         """
# #         Calculate the sum of the squares of the differences between the x and y
# #         coordinates.
# #         Returns:
# #         float: The sum of the squared differences between the x and y coordinates.
# #         """
# #         dif_x = x_a - x_b
# #         dif_y = y_a - y_b
# #         pow_diff_x = math.pow(dif_x, 2)
# #         pow_diff_y = math.pow(dif_y, 2)
# #         global sum_pow
# #         sum_pow = pow_diff_x + pow_diff_y
# #         return sum_pow
# #     square_difference()
# #     dist = math.sqrt(sum_pow)
# #     return dist
# # # Print the result
# # result = calculate_disttance()
# # print('%.2f' % result)


