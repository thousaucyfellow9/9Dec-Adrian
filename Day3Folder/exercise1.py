'''
Write a program to ask the user to enter a password.

If the password is correct, say "Access Granted"

Else, say "Access Denied"

The user is given a change to enter the password 3 times until the correct password is given.
If the user fails the 3rd attempt, the program will say "System Locked. I call police."

'''


answer = input("What is the password?")

if answer == "passme":
    print("Access granted")
else:
    print("WRONG PASSWORD")


    
