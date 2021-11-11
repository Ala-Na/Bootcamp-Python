def ft_filter(function_to_apply, iterable):
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