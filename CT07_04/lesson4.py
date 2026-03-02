print("Hello from lesson 4")

# ## Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list

# ---------------------------------------------------------------

# ## Task 2: List of planets (part 2)
# Tasks:

# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or changed name), print
#    "<planet name> : I conquered this"
# 4. If name == "Lalaland", print
#    "<planet name> : I created this"

# ---------------------------------------------------------------

# ## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ... 

# ---------------------------------------------------------------

# ## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# print(planets)
# planets[3] = "death to humans i hate humans and i will crash mars into earth"
# planets.insert(3, "Mars 1.0")
# planets.append("Pluto")
# planets.insert(20, "Pluto 1.0")
# print(planets)
# del planets[7]
# print(planets)planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# print(planets)
# print("goodbye my dear Jupiter but destroying you is the first step to destroy humanity")
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune","lalaland" ]
# print(planets)
# print(planets)
# # planets[2] = "this is my home"
# for planet in planets:
#     print(planet)
#     if planet == "Earth":
#         print(planet + ": this is my home")
#     elif planet == "Mars":
#         print(planet + ": I conquered this")
#     elif planet == "Lalaland":
#         print(planet + ": I created this")



# # Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each fooitem into the menu list
# 3. End the loop when the user types "end"

# menu = []

# while True:
#     item=input("Please enter a food item for the menu (type 'end' to finish): ")
#     if item.lower() == 'end':
#         break
#     menu.append(item)
# print("Restaurant Menu:")
# for item in menu:
#     print(item)

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."
#keep asking the customer until they said they will go next door
menu = []

while True:
    item=input("what would you like to eat (type 'we will go next door' to finish): ")
    if item.lower() == 'we will go next door':
        break
    menu.append(item)
menu = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
while item != 'we will go next door':
    if item in menu:
        print("Yes we sell that, please have a seat.")
    else:
        print("Sorry, please go next door, bye.")
   

#keep asking the customer until they said they will go next door






