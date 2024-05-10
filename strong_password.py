# Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least 6.
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+
# She typed a random string of length n in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

# Note: Here's the set of types of characters in a form you can paste in your solution:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
# Example

# password = '2bbbb'
# This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is 2.

# password = '2bb#A'
# This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is 1.

# Function Description

# Complete the minimumNumber function in the editor below.

# minimumNumber has the following parameters:

# int n: the length of the password
# string password: the password to test
# Returns

# int: the minimum number of characters to add

# nput Format

# The first line contains an integer , the length of the password.

# The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

# Sample Input 0

# 3
# Ab1
# Sample Output 0

# 3


# Explanation 0

# She can make the password strong by adding 3 characters, for example, $hk, turning the password into Ab1$hk which is strong.

# 2 characters aren't enough since the length must be at least 6.

# Sample Input 1

# 11
# #HackerRank
# Sample Output 1

# 1
# Explanation 1

# The password isn't strong, but she can make it strong by adding a single digit.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+" 

    is_upper = False
    is_lower = False
    is_digit = False
    is_special = False
    missing_character =0

    for i in password:
        if i in numbers:
            is_digit = True
        if i in lower_case:
            is_lower = True
        if i in upper_case:
            is_upper = True
        if i in special_characters:
            is_special = True
            
    if not is_upper:
        missing_character +=1
    if not is_lower:
        missing_character +=1
    if not is_digit:
        missing_character +=1
    if not is_special:
        missing_character +=1
    
    if n<6:
        return max(6-n, missing_character)
    else:
        return missing_character
    
     

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
