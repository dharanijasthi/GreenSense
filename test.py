
import math

def create_large_list():
    large_list = list(range(1000000))
    return large_list

def factorial(n):
    return math.factorial(n)

def give_output(n):
    if n <= 1:
        return n
    else:
        return give_output(n-1) + give_output(n-2)
    
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
