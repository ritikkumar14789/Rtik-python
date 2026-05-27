"""
=================================================
LEAP YEAR CHECKER
=================================================

Problem Statement:
Write a Python program to check whether
a year is a leap year or not.

-------------------------------------------------
Conditions:
1. Year divisible by 400 -> Leap Year
2. Year divisible by 4 and not by 100 -> Leap Year
3. Otherwise -> Not a Leap Year

-------------------------------------------------
Input Example:
2024

Output Example:
2024 is a Leap Year

-------------------------------------------------
Hints:
Use modulo operator (%)

=================================================
"""

# Take input from user
year = int(input("Enter a year: "))

# Check leap year
if year % 400 == 0:
    print(year, "is a Leap Year")

elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")

else:
    print(year, "is Not a Leap Year")