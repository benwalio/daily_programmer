# Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
# For extra credit, have the user and password in a seperate .txt file.
# for even more extra credit, break into your own program :)

input_password = raw_input("Please enter your password - ")
input_username = raw_input("Please enter your username - ")

auth_file = open("5_auth.txt","r")
