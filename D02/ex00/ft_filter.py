def ft_filter(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_filter received a non iterable object as second argument.")
        return None
    if callable(function_to_apply) is False:
        print("ft_filter received a non function argument as first argument.")
        return None
    for value in iterator:
        if (function_to_apply(value)):
            yield value
