# Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
# For extra credit, have the user and password in a seperate .txt file.
# for even more extra credit, break into your own program :)
import sys

authenticated = 0

input_password = raw_input("Please enter your password - ")
input_username = raw_input("Please enter your username - ")

auth_file = open("5_auth.txt","r")

auth_username, auth_password = auth_file.read().split(",")
# split_auth = auth_file_line

# auth_username = split_auth[0]
# auth_password = split_auth[1]

if input_username == auth_username:
    print "username match"
else:
    print "username mismatch"
    sys.exit()

if input_password == auth_password:
    print "password match"
else:
    print "password mismatch"
    sys.exit()

if input_username == auth_username and input_password == auth_password:
    authenticated = 1
else:
    sys.exit()

print authenticated
