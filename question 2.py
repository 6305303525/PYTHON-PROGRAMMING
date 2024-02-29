def my_func(x):
    if x<0:
        return 1
    return x * my_func(x-1)
x=int(input())
print(my_func(x))
