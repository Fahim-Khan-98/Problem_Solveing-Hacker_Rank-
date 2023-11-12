# Problem:
# Alice wrote a sequence of words in CamelCase as a string of letters,s , having the following properties:

# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given s, print the number of words in s on a new line.

# For example, s=oneTwoThree There are 3 words in the string.

# Function Description

# Complete the camelcase function in the editor below. It must return the integer number of words in the input string.

# camelcase has the following parameter(s):

# s: the string to analyze
# Input Format

# A single line containing string s

# .

# Constraints

# i<|s|<10^5
# Output Format

# Print the number of words in string s

# .

# Sample Input

# saveChangesInTheEditor
# Sample Output

# 5
# Explanation

# String s contains five words:

# save
# Changes
# In
# The
# Editor
# Thus, we print 5 on a new line.


# HackerRank Solution
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    upper= 0
    for i in s:
        if i.islower():
            pass
        else:
            upper +=1
    return upper+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()












# Test Purpose
STR = "secGeeksForGeeks"
upper=0
lower=0
for i in STR:
    if i.islower():
        lower +=1
    else:
        upper +=1
print("upper ",upper)
print("lower ",lower)
print("CamelCase ",upper+1)