def ft_filter(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_filter received a non iterable object as second argument.")
        return None
    try:
        callable(function_to_apply)
    except:
        print("ft_filter received a non function argument as first argument.")
        return None
    for value in iterator:
        if (function_to_apply(value)):
            yield value

x = [1, 2, 3, 4, 5]
print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))
print("")
print(filter(lambda dum: not (dum % 2), x))
print(list(filter(lambda dum: not (dum % 2), x)))