
def create_large_list():
    large_list = list(range(1000000))
    return large_list

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def give_output(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b
