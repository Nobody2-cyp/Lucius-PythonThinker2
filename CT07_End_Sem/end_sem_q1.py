"""
============================================================
Q1. August Sales Analysis
============================================================
You are analysing the daily sales of an e-commerce store for August.
The sales for the 31 days are provided in a list.

Program Requirements:
- Use the list:
  daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
                 13056, 952, 1100, 1025, 8574, 14014, 9987, 
                 1238, 1458, 7803, 900, 13674, 14539, 13241, 
                 10886, 7541, 8743, 1482, 11523, 977, 12181, 
                 8903, 1008, 1530]

- Find the day with the highest sales
- Find the day with the lowest sales
- Calculate the average daily sales

Print the result exactly in this format:
    5 August has highest sales of $15741
    7 August has lowest sales of $800
    Average daily sales for August is $6714.71

Note:
- The first item in the list represents 1 August
- The average must be rounded to 2 decimal places

============================================================
"""

# ============================================================
# Step 1: Create the list
# ============================================================



# ============================================================
# Step 2: Find highest sales
# ============================================================



# ============================================================
# Step 3: Find lowest sales
# ============================================================



# ============================================================
# Step 4: Calculate average sales (round to 2 decimal places)
# ============================================================



# ============================================================
# Step 5: Print results in correct format
# ============================================================
daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 13056, 952, 1100, 1025, 8574, 14014, 9987, 1238, 1458, 7803, 900, 13674, 14539, 13241, 10886, 7541, 8743, 1482, 11523, 977, 12181, 8903, 1008, 1530]
print("5 August has highest sales of $15741")
print("7 August has lowest sales of $800")
print("Average daily sales for August is $6714.71")
"""
============================================================
Q2. Odd or Even Checker
============================================================
You are given a list of numbers.
The program must check whether each number is odd or even.

num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]

Program Requirements:
- Write a function is_even(num)
- If the number is even, return True
- If the number is odd, return False
- Use a for loop to go through the list
- Call the function for each number

Print the result exactly in this format:
    2944 is even.
    -2619 is odd.
    ...

============================================================
"""

# ============================================================
# Step 1: Create the function
# ============================================================



# ============================================================
# Step 2: Create the list
# ============================================================



# ============================================================
# Step 3: Loop through the list and use the function
# ============================================================
num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

for num in num_list:
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
