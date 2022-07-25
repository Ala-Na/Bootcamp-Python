from NumPyCreator import NumPyCreator

npc = NumPyCreator()

lst = [[1,2,3],[6,3,4]]
print(npc.from_list(lst))
print("")

print(npc.from_list([[1,2,3],[6,4]]))
print("")

res = (npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
print(res, "dtype='", res.dtype, "'")
print("")

print(npc.from_list((1,2),(3,4)))
print("")

print(npc.from_tuple(("a","b","c")))
print("")

print(npc.from_tuple([[1,2,3],[6,3,4]]))
print("")

print(npc.from_iterable(iter(range(5))))
print("")

shape=(3,5)
print(npc.from_shape(shape))
print("")

print(npc.random(shape))
print("")

print(npc.identity(4))
