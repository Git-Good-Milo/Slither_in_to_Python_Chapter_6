# # Question 1
# # Write a program that takes as input, a single integer from the user which will specify how many decimal places the number e should be formatted to.
#
# # First step is to get the user to initialise a number for the precision
# # And save the value of e to a variable
# user_input = int(input("Please enter a number for precision: "))
# e = 2.7182818284590452353602874713527
#
# # Next step is write the print script that will print e to the user input number of places.
# print("{:.{}f}".format(e, user_input))

# Question 2
# Write a program that will take as input, a string and two integers. The two integers will represent indices. If the string can be sliced using the two indices then print the sliced string. If either or both of the integers are outside the strings index range then print that the string cannot be sliced at those integers.

# # First we specify user_inputs for a string and 2 integers for the index
# user_input_string = input("Please enter a string: ")
# user_input_num1 = int(input("Please enter your first index: "))
# user_input_num2 = int(input("Please enter your second index: "))
#
# # Next we write a script containing conditional statements about the indices and strings
# # We will also need a while loop to prevent negative numbers from being used
#
# if len(user_input_string) <= user_input_num1 and len(user_input_string) <= user_input_num2:
#     print("The indices are too big to slice the string")
# elif len(user_input_string) > user_input_num1 and len(user_input_string) > user_input_num2:
#     print(f"Your string {user_input_string} can be sliced! Here is your output: ")
#     print()
#     print(user_input_string[user_input_num1:user_input_num2])

# Question 3
# When you sign up for accounts on website or apps, you may be told your password strength when entering it for the first time. In this exercise, you are to write a program that takes in as input, a string that will represent a password.

# First we specify the user_input_pass, initialise a counter for the password, and initialise a counter to iterate through the password
user_input_pass = input("Please enter your password: ")
pass_strength = 0

# Generate a list of special characters
special_list = ["$", "#", "@", "^", "£", "!", "%", "*" ]

# Next we need so specify some conditional statements to see what characters the password contains

# for character in user_input_pass:
#     if character.isupper():
#         pass_strength += 1
#         break
# for character in user_input_pass:
#     if character.islower():
#         pass_strength += 1
#         break
# for character in user_input_pass:
#     if character.isnumeric():
#         pass_strength += 1
#         break
# for character in user_input_pass:
#     for index in special_list:
#         if character == index:
#             pass_strength += 1
#             break
#
# print(f"You password strength is {pass_strength}")
# if int(pass_strength) == 4:
#     print("You password is strong enough")
# elif int(pass_strength) < 4:
#     print("Sorry your password is not strong enough")

# Question 4
# Write a program that takes 3 floating point numbers as input from the user: a starting radius, radius increment and an ending radius. Based on these three numbers, your program should output a table with a spheres corresponding surface area and volume.

