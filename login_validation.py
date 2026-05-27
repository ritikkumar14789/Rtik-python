"""
=================================================
LOGIN VALIDATION SYSTEM
=================================================

Problem Statement:
Write a Python program to validate login
using username and password.

-------------------------------------------------
Conditions:
1. Correct username and password -> Login Successful
2. Wrong username or password -> Invalid Login

-------------------------------------------------
Input Example:
Username: admin
Password: 1234

Output Example:
Login Successful

=================================================
"""

# Correct username and password
correct_username = "admin"
correct_password = "1234"

# Take input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Validate login
if username == correct_username and password == correct_password:
    print("Login Successful")

else:
    print("Invalid Username or Password")