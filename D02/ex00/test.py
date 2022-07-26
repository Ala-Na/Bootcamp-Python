from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce
import functools

function = lambda x: x + 1
iterable = [1, 2, 3]

print("--- Filter ---")
x = [1, 2, 3, 4, 5]
print("Mine :")
print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))
print("\nOriginal :")
print(filter(lambda dum: not (dum % 2), x))
print(list(filter(lambda dum: not (dum % 2), x)))
print("\nMore :")
print(ft_filter(function_to_apply = None, iterable = iterable))
print(list(ft_filter(function_to_apply = None, iterable = iterable)))
print(list(ft_filter(lambda x: x <= 1, [])))


print("\n--- Map ---")
print("Mine :")
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda t: t + 1, x)))
print("\nOriginal :")
x = [1, 2, 3, 4, 5]
print(map(lambda dum: dum + 1, x))
print(list(map(lambda t: t + 1, x)))
print("\nMore :")
print(ft_map(function_to_apply = None, iterable = iterable))
print(list(ft_map(function_to_apply = None, iterable = iterable)))
print(list(ft_map(lambda x: x + 2, [])))
print(list(ft_map(lambda x: x + 2, [1])))
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

print("\n--- Reduce ---")
print("Mine :")
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
print("\nOriginal :")
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(functools.reduce(lambda u, v: u + v, lst))
print("\nMore :")
print(ft_reduce(None, iterable = iterable))
print(ft_reduce(function, None))
print(ft_reduce((lambda x, y: x + y), [1]))
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))
