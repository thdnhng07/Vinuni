# test = 'hello'
# def reverse(test):
#     test = list(test)
#     text = ''
#     for i in range(len(test)-1, -1, -1):
#         text += test[i]
#     return text

# print(reverse(test))

# num = 100

# def find_prime(num):
#     n = 0
#     prime_num = []
#     arr = list(range(num + 1))

#     for i in arr:
#         if arr[i] > 1:
#             for j in range(2, arr[i]):
#                 if (arr[i] % j) == 0:
#                     break
#             else:
#                 prime_num.append(arr[i])
#     return prime_num

# print(find_prime(num))

# class BankAccount:

#     def __init__(self, account_number,balance):

#         self.balance = balance
#         self.account_number = account_number

#     def deposit(self, amount: float):
#         if amount > 0:
#             self.balance += amount
#         else:
#             raise ValueError
    
#     def withdraw(self, amount: float):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#         else:
#             raise ValueError
    
#     def get_balance(self):
#         return self.balance
    

# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         self.balance += self.balance * self.interest_rate

# class CurrentAccount(BankAccount):
#     def __init__(self, account_number, balance, overdraft_limit):
#         super().__init__(account_number, balance)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount: float):
#         if amount > 0 and amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#         else:
#             raise ValueError
        
# # Create accounts
# account = BankAccount(101, 500)
# savings = SavingsAccount(102, 1000, 0.05)

# # Perform operations
# account.deposit(200)  # Balance: 700
# account.withdraw(300)  # Balance: 400
# savings.deposit(500)  # Balance: 1500
# interest = savings.calculate_interest()  # Interest: 75.0
# print(account.get_balance(), savings.get_balance(), interest)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# import tkinter as tk
# from tkinter import ttk

# window2 = tk.Tk()
# window2.geometry('500x500')
# window2.title("Converter")

# km = tk.DoubleVar()
# km.set(0)
# miles = tk.DoubleVar()

# def convert(*args):
#     miles.set('%.3f' % (km.get() / 1.6))

# km.trace_add('write', convert)
# miles.trace_add('write', convert)

# text1 = ttk.Label(window2, text="Enter the number of km: ", font=('Calibra', 15, 'bold'))
# text1.grid(row=0, column=0)

# input = ttk.Entry(window2, width=20, textvariable=km)
# input.grid(row=0, column=4)

# text2 = ttk.Label(window2, text="Miles: ", font=('Calibra', 15, 'bold'))
# text2.grid(row=1, column=0)

# # Print out the result
# text3 = ttk.Label(window2, textvariable=miles, font=('Calibra', 15, 'bold'))
# text3.grid(row=1, column=1)

# window2.mainloop()


# import numpy as np

# print(np.arange(0, 10,2))
# print(np.linspace(0, 1))

# print(np.random.rand(2, 3))

# tuple = (0,1, 2, 4, 5, 6, 7)

# if any(tuple) == 1:
#     print(1)


# def find_subsets(nums: list) -> list:
#     if nums == []:
#         return [[]]
    
#     subsets = find_subsets(nums[1:])
#     return subsets + [subset + [nums[0]] for subset in subsets]

# nums = [1, 2]
# print(find_subsets(nums))  # Expected: [[], [1], [2], [1, 2]]

# import pandas as pd

# # 1. Create a DataFrame with some sample data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, None, 28],
#     'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo']


# df = pd.DataFrame(data)

# # 2. Display the DataFrame to see the original data
# print("Original DataFrame:")
# print(df)

# # 3. Handling missing data (e.g., filling missing age with the mean age)
# mean_age = df['Age'].mean()
# df['Age'].fillna(mean_age, inplace=True)

# # 4. Sorting the data by Age
# df_sorted = df.sort_values(by='Age')

# # 5. Filter the DataFrame to get people older than 30
# df_filtered = df[df['Age'] > 30]

# # 6. Show the modified DataFrame and the filtered data
# print("\nDataFrame after filling missing values and sorting by Age:")
# print(df_sorted)

# print("\nFiltered DataFrame (Age > 30):")
# print(df_filtered)

# # 7. Save the modified DataFrame to a new CSV file
# # df_sorted.to_csv('sorted_data.csv', index=False)

# # Indicate that the data has been saved
# print("\nThe sorted data has been saved to 'sorted_data.csv'.")

# def remove_adjacent_duplicates(prompt):
#     result = []
#     i = 0

#     while i < len(prompt):
#         if i < len(prompt) - 1 and prompt[i] == prompt[i + 1]:
#             while i < len(prompt) - 1 and prompt[i] == prompt[i + 1]:
#                 i += 1
#         else:
#             result.append(prompt[i])
#         i += 1

#     if result == prompt:
#         return result
#     return remove_adjacent_duplicates(result)

# prompt = list('geeksforgeek')
# print(''.join(remove_adjacent_duplicates(prompt)))


# def recursion_print(n):

#     string = 'I love Recursion'

#     if n > 0:
#         print(string)
#         recursion_print(n - 1)

# n = int(input())
# recursion_print(n)



# def print_n(n):

#     if n > 0:
#         print_n(n - 1)
#         print(n)
# n = int(input())
# print_n(n)

# def print_n(n):
#     if n == 0:
#         return []
#     else:
#         result =[n] + print_n(n - 1)
#         return result
        

# n = int(input())
# print(*print_n(n))

# def print_even_indices(n, arr):
#     i = n - 1

#     if i < 0:
#         return
#     if i % 2 == 0:
#         global result
#         result.append(arr[i])
    
#     print_even_indices(n - 1, arr)

# n = int(input())
# arr = list(map(int, input().split()))

# result = []
# print_even_indices(n, arr)
# print(*result)

# def sequence(n):
#     if n == 1:
#         return [1]

#     if n % 2 == 0:
#         return [n] + sequence(n//2)

#     else:
#         return [n] + sequence(3 * n + 1)

# n = int(input())
# print(len(sequence(n)))

# def count_vowels(string, i=0):
#     vowels = 'aeiou'
#     if i == len(string):
#         return 0

#     if string[i].lower() in vowels:
#         return 1 + count_vowels(string, i + 1)
#     else:
#         return count_vowels(string, i + 1)

# string = input()
# print(count_vowels(string))

# def factorial(n):

#     if n == 0:
#         return 1
    
#     else:
#         return n * factorial(n - 1)

# n = int(input())    
# print(factorial(n))
import time
def knapsack(N, W, sub, index=0, max_value=0):

    if index == len(sub):
        return max_value

    current_sub = sub[index]
    
    total_weight = sum(item[0] for item in current_sub)
    total_value = sum(item[1] for item in current_sub)
    
    if total_weight <= W:
        max_value = max(max_value, total_value)

    return knapsack(N, W, sub, index + 1, max_value)

def create_subsequence(arr):
    dp = [[] for _ in range(len(arr) + 1)]
    dp[0] = [[]]

    for i in range(1, len(arr) + 1):
        dp[i] = dp[i - 1] + [seq + [arr[i - 1]] for seq in dp[i - 1]]

    return [seq for seq in dp[-1] if seq]

N, W = map(int, input().split())
w_to_v = []
for _ in range(N):

    w, v = map(int, input().split())
    w_to_v.append([w, v])

items_weight = [items[0] for items in w_to_v]

sub = create_subsequence(w_to_v)
start = time.perf_counter()
print(knapsack(N, W, sub))
end = time.perf_counter()
print(f"Time taken: {end - start} seconds")
