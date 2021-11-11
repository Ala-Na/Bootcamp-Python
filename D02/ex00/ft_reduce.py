import functools

def ft_reduce(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_reduce received a non iterable object as second argument.")
        return None
    try:
        callable(function_to_apply)
    except:
        print("ft_reduce received a non function argument as first argument.")
        return None
    value = next(iterator)
    for element in iterator:
        value = function_to_apply(value, element)
    return value

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
print("")
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(functools.reduce(lambda u, v: u + v, lst))
