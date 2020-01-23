# Question 1
# Write a program that takes as input, a single integer from the user which will specify how many decimal places the number e should be formatted to.

# First step is to get the user to initialise a number for the precision
# And save the value of e to a variable
user_input = int(input("Please enter a number for precision: "))
e = 2.7182818284590452353602874713527

# Next step is write the print script that will print e to the user input number of places.
print("{:.{}f}".format(e, user_input))

# Question 2
# Write a program that will take as input, a string and two integers. The two integers will represent indices. If the string can be sliced using the two indices then print the sliced string. If either or both of the integers are outside the strings index range then print that the string cannot be sliced at those integers.

# First we specify user_inputs for a string and 2 integers for the index
user_input_string = input("Please enter a string: ")
user_input_num1 = int(input("Please enter your first index: "))
user_input_num2 = int(input("Please enter your second index: "))

# Next we write a script containing conditional statements about the indices and strings

if len(user_input_string) <= user_input_num1 and len(user_input_string) <= user_input_num2
    print("The indices are too big to slice the string")