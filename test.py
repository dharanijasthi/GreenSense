
import numpy as np

def create_large_list():
    large_list = list(range(1000000))
    return large_list

def factorial(n):
    return np.math.factorial(n)

def give_output(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b

def subArraySum(arr, n, sum):
    for i in range(0,n):
        currentSum = arr[i]
        if(currentSum == sum):
            return
        else:
            for j in range(i+1,n):
                currentSum += arr[j]
                if(currentSum == sum):
                    return
