def ft_map(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_map received an not iterable object.")
        return None
    i = 0
    while i < len(iterable):
        iterable[i] = function_to_apply(iterable[i])
        yield iterable[i]
        i += 1

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))
print("")

x = [1, 2, 3, 4, 5]
print(map(lambda dum: dum + 1, x))
print(list(map(lambda t: t + 1, x)))