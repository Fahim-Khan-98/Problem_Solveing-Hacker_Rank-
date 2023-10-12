# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# """"""
# The unique element is .

# Function Description

# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the element that occurs only once
# Input Format

# The first line contains a single integer, , the number of integers in the array.
# The second line contains  space-separated integers that describe the values in .

# Constraints

# It is guaranteed that  is an odd number and that there is one unique element.
# , where .
# Sample Input 0

# 1
# 1
# Sample Output 0

# 1
# Explanation 0

# There is only one element in the array, thus it is unique.

# Sample Input 1

# 3
# 1 1 2
# Sample Output 1

# 2
# Explanation 1

# We have two 's, and  is unique.

# Sample Input 2

# 5
# 0 0 1 2 1
# Sample Output 2

# 2
# Explanation 2

# We have two 's, two 's, and one .  is unique.











#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(arr):
    # Write your code here
    double_val = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] == arr[j]):
                double_val.append(arr[i])
    a = [x for x in arr if x not in double_val]
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    result_string = ', '.join(map(str, result))

    fptr.write(str(result_string) + '\n')

    fptr.close()


# Another solution


def find_unique_value(arr):
    unique_values = []
    for value in arr:
        if arr.count(value) == 1:
            unique_values.append(value)
    return unique_values

arr = [1, 2, 3, 4, 1, 2, 3,7,8]
result = find_unique_value(arr)

result_string = ', '.join(map(str, result))
print(result_string)