def create_large_list():
    large_list = []
    for i in range(1000000):
        large_list.append(i)
    return large_list

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def give_output(n):
    if n <= 1:
        return n
    else:
        return give_output(n-1) + give_output(n-2)