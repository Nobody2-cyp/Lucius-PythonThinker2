print("Hello from lesson 2")

## Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24
i = 0
while i < 21: 
    print(i)
    i = i + 1

i = 1
while i < 31:
    print(i)
    i = i + 1

i = 2
while i < 25:
    print(i)
    i = i + 1

## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.

# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop
i = 1
while i < 11:
    if i == 5:
        break
    print(i)
    i = i + 1

# print 50 to 25
i = 50
while i > 24:
    print(i)
    i = i - 1

# print 100 to 86 only even number
i = 100
while i > 85:
    print(i)
    i = i - 2

# print only those that are multiple of 3, 4, 5 from 100 to 25 in a while loop

## Task 3: while... else
# The else condition will run when the loop exits normally
# i.e. when the while condition is no longer true.

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.

i = 1
while i < 11:
    print(i)
    i = i + 1
else:
    print("Count has reached 10")

i = 1
while i < 11:
    if i == 5:
        break
    print(i)
    i = i + 1
else:
    print("Count has reached 10") 

# print only those that are multiple of 3, 4, 5 from 100 to 25 in a while loop
# i = 100
# while i > 24:
#     if i % 3 == 0 or i % 4 == 0 or i % 5 == 0:
#         print(i)
#     i = i - 1




## Task 4: Ordering Pizzas with while loop
# **Task: Using what you have learned above, code a program to
# take a customer's order for pizza.
# Declare a variable called _topping_.**

# Using a while loop:
# 1. Ask the user to enter a choice of topping
# 2. For each topping entered, concatenate to the 'topping'
#    variable
# 3. exit the while loop if the user enters "end"
# 4. On program end, print out the toppings that the customer
#    has chosen.
# input("welcome to my pizza shop what topping would you like for your pizza?" )
topping = ""
while True:

    toppings = input("Enter a topping (or 'end' to finish): ")
    topping += toppings + " "
    if toppings.lower() == "end":
        break
    
    print(f" i have added ${topping} to your pizza.")
print(f"your pizza is ready with the following toppings: ${topping}")
## Task 5: General Knowledge Quiz
**Task: Create a program to quiz users on their general
knowledge**

Using the while loop, ask 3 general knowledge questions
1. Using input ask the question
2. While answer is not correct, repeat the question.
3. Move on to the next question when the answer is correct

Bonus:
1. Add a score system
2. Add an ability for users to skip by saying “skip”
3. Disqualify user when they have tried too many times --> -->































