# print("Hello from lesson 5")

# # # Lesson 5 - List Variables II

# # ## Recap 1: Favourite Food List
# favourite_food_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# # **Recap 1a**:
# # Create a list of 5 food that you like to eat
# favourite_food_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"] 
# # **Recap 1a**:
# # **Recap 1b**:
# # You no longer like to eat the 3rd item on your list,
# # delete it
# favourite_food_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"] 
# del favourite_food_list[2]

# # **Recap 1c**:
# # Add 1 more item into your list
# favourite_food_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"] 
# favourite_food_list.append("Pluto")
# # **Recap 1d**:
# # Write a for loop to say all the food items in your list
# favourite_food_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Pluto"]
# for food in favourite_food_list:
#     print("I like to eat " + food)

## Task 1: List of 100 numbers 
# You are preparing for an upcoming lucky draw session at your
# school. You have been tasked to create a program that will pick
# 100 lucky winners.

# By importing the 'random' library and using 'random.randint()',
# create a program to create 100 random numbers in a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000

# ------------------------------------------------------------
import random
# lucky_draw_numbers = []

# for i in range(100):
#     
#     lucky_draw_numbers.append(random_random_number = random.randint(1, 1000)number)


# # Task 2: List of 100 unique numbers
# The program you have created from the previous task will
# sometimes generate duplicate numbers. Modify your program so
# that the 100 numbers generated are all unique.

# Modify your program from the previous task to create 100 random
# unique numbers in a list.
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique
# 4. Print the list of 100 unique numbers created

# Hint: Use a while loop to check if the number already exists in
# the loop
# while len(lucky_draw_numbers) < 100:
#     random_number = random.randint(1, 1000)
#     if random_number not in lucky_draw_numbers:
#         lucky_draw_numbers.append(random_number)
# print(lucky_draw_numbers)
# print(len(lucky_draw_numbers))

## Task 3: Score Taker
# Imagine the list that you have created in Task 2 represent the
# score of a 100 students.

# Find the maximum, minimum and average from the list.

# 1. Using the 'max()' function, find the maximum score.
# 2. Using the 'min()' function, find the minimum score.
# 3. Using the 'sum()' and 'len()' function, calculate the
#    average score.
# max_score = max(lucky_draw_numbers)
# min_score = min(lucky_draw_numbers)
# average_score = sum(lucky_draw_numbers) / len(lucky_draw_numbers)
# print("Maximum Score:", max_score)
# print("Minimum Score:", min_score)
# print("Average Score:", average_score)


## Task 4: Who is the tallest?
# Task: You are given 2 lists, 
# **namelist** contains a list of students in your class
# **heightlist** contains a list of the corresponding student's
#                height

# 1. Determine who is the tallest in class, and what is his/ her
#    name
# 2. Determine who is the shortest in class, and what is his/ her
#    name

# Sample Data (Copy + paste the below code):
# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# Hint:
# use .index("value of something in the list") to find the index
# of an item
# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan", "Sophia", "Lucas", "Mia", "Aiden"]           
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]
# max_height = max(heightlist)
# min_height = min(heightlist)
# tallest_Student_index = heightlist.index(max_height)
# shortest_Student_index = heightlist.index(min_height)
# print("The tallest student is " + namelist[tallest_Student_index] + " with a height of " + str(max_height) + " cm.")
# print("The shortest student is " + namelist[shortest_Student_index] + " with a height of " + str(min_height) + " cm.")


## Task 5: Pokemon, I choose you!
# Task: You are given 2 lists,
# **pokemons** contains a list of pokemons
# **powers** contains a list of the corresponding pokemon's
#            powers

# 1. Choose 2 random pokemons from the list
# 2. Compare the powers of the 2 pokemons
# 3. Calculate who is the winner of the fight between these 2
#    pokemons
#    (pokemon with the higher power will always win)

# Sample data (Copy + paste the below code):

pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"]
powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83]
random_pokemon1 = random.choice(pokemons)
random_pokemon1_index = pokemons.index(random_pokemon1)
random_pokemon2 = random.choice(pokemons)
random_pokemon2_index = pokemons.index(random_pokemon2)
print("Pokemon 1: " + random_pokemon1 + " with power " + str(powers[random_pokemon1_index]))
print("Pokemon 2: " + random_pokemon2 + " with power " + str(powers[random_pokemon2_index]))
if powers[random_pokemon1_index] > powers[random_pokemon2_index]:
    print(random_pokemon1 + " wins!")
elif powers[random_pokemon2_index] > powers[random_pokemon1_index]:
    print(random_pokemon2 + " wins!")
else:
    print("It's a tie!") 

# are you able to prevent two of the same pokemon from fighting one another?
import random
poke1 = random.choice(pokemons)
poke2 = random.choice(pokemons) 
poke1_ind = pokemons.index(poke1)
poke2_ind = pokemons.index(poke2)
poke1_power = powers[poke1_ind]
poke2_power = powers[poke2_ind]
if poke1 == poke2_power:
    print("It's a tie.")
elif poke1_power > poke2_power:
    print(poke1 + " wins.")
else:
    print(poke2 + " wins.")




 nested_list = []
 

        



















