"""
=================================================
ODD AND EVEN NUMBER CHECKER
=================================================

Problem Statement:
Write a Python program to check whether a
number is odd or even.

-------------------------------------------------
Condition:
1. If number is divisible by 2 -> Even
2. Otherwise -> Odd

-------------------------------------------------
Input Example:
7

Output Example:
7 is Odd

-------------------------------------------------
Hints:
Use modulo operator (%)

=================================================
"""

# Take input from user
num = int(input("Enter a number: "))

# Check odd or even
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")