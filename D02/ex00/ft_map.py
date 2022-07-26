def ft_map(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_map received a non iterable object as second argument.")
        return None
    if callable(function_to_apply) is False:
        print("ft_map received a non function argument as first argument.")
        return None
    for value in iterator:
        yield function_to_apply(value)
