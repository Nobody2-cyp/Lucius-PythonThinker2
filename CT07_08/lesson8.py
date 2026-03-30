
student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# Task​

# Given a list of student index numbers (with duplicates), create a cleaned list where each
# student appears once.​

# Sort the cleaned list in ascending order.​

# Print the final list and also print how many duplicates were removed.​

# Print the count of how many students attended the Math Enrichment Class.
# sort = sorted(student_indexes)
# print(sort)
# unique= []
# duplicates = 0
# for student in student_indexes:
#     if student not in unique:
#         unique.append(student)
#     else:
#         duplicates += 1

# first_name = "" 
# while not first_name.isalpha():
#     first_name = input("what is your first name? : ")
# print(first_name)
    
# Task 1a
# # Ask the user to input their first name until it is a valid name. ​
# A valid name only contains alphabets.​
# Keep asking for a name until a valid name is input.​

# Task 1b
# Ask the user to input their age until it is a valid number. ​
# Keep asking for a name until a valid number is input.​

# Task 1c
# Ask the user to input a valid username. A valid username must contain
# alphabets and numbers, but not contain special characters​
# first_name = "" 
# while not first_name.isalpha():
#     first_name = input("what is your first name? : ")
# print(first_name)

# age = ""
# while not age.isalnum():
#     age = input("what is your age? :")
    # print(age)
    # valid_username = ""
    # while not valid_username.isalnum():
    #     valid_username = in
# while True:
#     username = input("what is the username?")
#     if username.isalpha() or username.idigit():
#         print("username must contain alphabets and numbers.")
#         if username.isalnum() and not username.isalpha() and not username.isdigit 
#         break 
# print(username)
    
          
# Task 2a​
# Ask the user to input their phone number until it is valid using
# a while loop.​
# Make sure to check if the input is the correct data type as well!​

# Task 2b​
# Ask the user to a username and check if it is between 5 to 18
# characters long.​
# phone_number = ""
# while not phone_number.isalnum() or len(phone_number) <8:
#     phone_number = input("what is your phone number? :")
#     print(phone_number)
#     while True:
#      username = input("what is the username?")
#      if username.isalpha() or username.idigit():
#        print("username must contain alphabets and numbers.")
# if username.isalnum() and not username.isalpha() and not username.isdigit 
#  break 
# print(username)

# # Lesson 8 - Input Validation

# ## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

# ## Task 1: Data Format Check

# ### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.

# ### Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# ### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# ## Task 2: Length Check (using a while loop)

# ### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!

# ### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.

# ## Task 3: Range Check (using a while loop)

# ### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year. 
# Keep asking until a correct value is given.
# birth_year = ""
# birth_year = input("please enter your birth year")
# while True:
#     if birth_year.isdigit() and birth_year >= 1900 and birth_year <= 2026:
#         print(birth_year)
#         break
#     else:
#         birth_year = input("please enter your birth year")
# ### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.
# while True:
#    volume = input("what is the volume?")
#    valid = True
#    if not volume.isdigit():
#       print("The volume should be digits")
#       continue
#    if not (int(volume) >0 and int(volume) <=100
#            print("the volume should be between 0 and 100")
#    if valid:
#       break

#    if valid:
#       break
#       print(f"")
# ## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.
# sentence = input("what is your sentence")
# new_sentence = ""
# is_upper = True
# for char in sentence:
#     if char.isaphla():
#         if is_upper():
#             new_sentence += char.upper()
#         else:
#             new_sentence += char.lower()
#             is_upper = not is_upper
#     else:
#         new_sentence += char
# print(new_sentence)



# ## Task 5: Slice String
# word = “SINGAPORE”
word = "SINGAPORE"
print(word[:4])
print(word[3:6])
print(word[5:])
print(word[::2])


# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE

# ## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.
# word = "charizard"
# print(word[::-1])

# while True:
#     word = input("what is the word?")
#     if word.lower() =="end":
#         break
#     if word == word[::-1]:
#         print(word+ " is a palindrome")
#     else:
#         print(word+ " is not a palindrome")
# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

# ## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# friends = ["Alice", "Bob", "Carl", "Dylan"]
# valid = True
# while True:
#     name = input("what is your name?")
#     if name in friends:
#         print("please come in")
#     else:
#         print("GET OUT")
 

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

# ## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

first_letter = ["S", "T", "F", "G", "M"]
is_first_letter_valid = False
is_first_letter_in_list = False
is_7digit_between_alphabet = False
is_9char_long = False

while True:
    nric = input("NRIC ?").strip()
    if nric =="":
        print("NRIC cannot be empty or blank")
        continue

    if len(nric) == "":
        is_9char_long = True
    else:
        print("NRIC should be 9 characters long")
        
    if nric[0].isupper() and nric[-1].isupper():
        is_first_letter_valid = True
    else:
        print("First and last character are alphabets in upper case")

    if nric[0] in first_letter:
        is_first_letter_in_list = True
    else:
        print("First letter must be S, T, F, G, or M.")

    if nric[1:8].isdigit():
        is_7digit_between_alphabet = True
    else:
        print("Have 7 digits between the alphabets")

    if is_7digit_between_alphabet and is_9char_long and is_first_last_char_upper and is_first_letter_in_list:
        break


# ## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria
is_8char_long = False
is_upper_case = False
is_lower_case = False
is_num = False
is_alnum = False
while True:
    password = input("what is your password?").strip()
    if password =="":
        print("password cannot be empty or blank")
        continue
    if len(password) >= 8:
    is_8char_long = True
    for char in password:
        if char.isupper():
            is_upper_case = True
        if char.islower():
            is_lower_case = True
        if char.isdigit():
            is_num = True
    if password.isalnum():
        is_alnum = True

    if is_8char_long and is_upper_case and is lower+


    



# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me


































































































































































































