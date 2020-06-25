hacker rank solution 1
#!/bin/python

import math
import os
import random
import re
import sys
import operator 
import numpy as np
import collections


def groupSort(arr):

    frequency = {} 
    size = len(arr)
    for i in range (0, size): 
        frequency[arr[i]] = frequency.get(arr[i], 0) + 1
    a = []   
    arr_size = len(arr) 
    for i in frequency: 
        output=(i, frequency[i])
        a.append(output)
   
    items = {} 
    for line in a :
            key, value = line[0], line[1]
            items[key] = value
    items =collections.OrderedDict(sorted(items.items()))
    items = dict(sorted(items.items(), key=operator.itemgetter(1),reverse=True))
    
    
    for i in items: 
        output=(i, items[i])
        yield(output)
if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = groupSort(arr)
    # print(result)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


All test passed 

soluttion 2
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPrimeStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
listOfPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def countPrimeStrings(s):
    def helper(s, n, i):
        # If we are down to last 1 digit
        if i == n-1:
            if int(s[i]) in listOfPrimes:
                return 1
            else:
                return 0
        # If we are down to last 2 digits
        if i == n-2:
            if int(s[i:]) in listOfPrimes:
                return 1
            else:
                return 0
        else:
            # If single digit is prime, then place breakpoint here
            if int(s[i:i+1]) in listOfPrimes:
                return 1 + helper(s, n, i+1)
            # If two digits make a prime, then place breakpoint here
            if int(s[i:i+2]) in listOfPrimes:
                return 1 + helper(s, n, i+2)
    n = len(s)
    return helper(s, n, 0)


#
  
#     # Write your code here
if __name__ == '__main__':

only 2 test passed 
