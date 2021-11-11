def ft_map(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_map received a non iterable object as second argument.")
        return None
    try:
        callable(function_to_apply)
    except:
        print("ft_map received a non function argument as first argument.")
        return None
    for value in iterator:
        yield function_to_apply(value)

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))
print("")

x = [1, 2, 3, 4, 5]
print(map(lambda dum: dum + 1, x))
print(list(map(lambda t: t + 1, x)))