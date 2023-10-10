# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# arr = [1,3,5,7,9]

# The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of 5 integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints

# 1<=arr[i]<=10^9

# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14
# Explanation

# The numbers are 1, 2, 3, 4, and 5. Calculate the following sums using four of the five integers:

# Sum everything except 1, the sum is 2+3+4+5 .
# Sum everything except 2, the sum is 1+3+4+5.
# Sum everything except 3, the sum is 1+2+4+5.
# Sum everything except 4, the sum is 1+2+3+5.
# Sum everything except 5, the sum is 1+2+3+4.
# Hints: Beware of integer overflow! Use 64-bit Integer.

####Solution


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    
    a = sorted(arr)

    print(sum(a[:4]),sum(a[1:]))
   

    # a=0
    # b=0
    # max_val = max(arr)
    # min_val = min(arr)
    
    # arr1 = [x for x in arr if x!=max_val]
  
    # for i in arr1:
    #     a +=i
        
    
    
    # arr2 = [x for x in arr if x!=min_val]
    
    # for x in arr2:
    #     b +=x
    # print("{0} {1}".format(a,b))
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)




# easy another Solution

# def miniMaxSum(arr):
#     total_sum = sum(arr)
    
#     mini_sum = total_sum - min(arr)
#     max_sum = total_sum - max(arr)
#     print(max_sum, mini_sum)