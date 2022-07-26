def ft_reduce(function_to_apply, iterable):
    try:
        iterator = iter(iterable)
    except:
        print("ft_reduce received a non iterable object as second argument.")
        return None
    if callable(function_to_apply) is False:
        print("ft_reduce received a non function argument as first argument.")
        return None
    value = next(iterator)
    for element in iterator:
        value = function_to_apply(value, element)
    return value
