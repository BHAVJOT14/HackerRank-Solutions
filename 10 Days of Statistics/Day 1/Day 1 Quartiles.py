#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)

    length_Of_Array = len(arr)

    first_Number = length_Of_Array // 2
    second_Number = first_Number // 2
    third_Number = first_Number + second_Number

    if(length_Of_Array % 2 != 0):
        if(first_Number % second_Number != 0):
            q1 = arr[second_Number]
            q2 = arr[first_Number]
            q3 = arr[third_Number + 1]

            return q1, q2, q3
        else:
            q1 = (arr[second_Number - 1] + arr[second_Number]) // 2
            q2 = arr[first_Number]
            q3 = (arr[third_Number] + arr[third_Number + 1]) // 2

            return q1, q2, q3
    elif(length_Of_Array % 2 == 0):
        if(first_Number % second_Number != 0):
            q1 = arr[second_Number]
            q2 = (arr[first_Number] + arr[first_Number - 1]) // 2
            q3 = arr[third_Number]

            return q1, q2, q3
        else:
            q1 = (arr[second_Number - 1] + arr[second_Number]) // 2
            q2 = (arr[first_Number] + arr[first_Number - 1]) // 2
            q3 = (arr[third_Number] + arr[third_Number - 1]) // 2

            return q1, q2, q3



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
