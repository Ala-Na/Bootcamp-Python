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

print("\nErrors checks:")
print(npc.from_list("toto"))
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
print(npc.from_tuple(3.2))
print(npc.from_tuple(((1,5,8),(7,5))))
print(npc.from_shape((-1, -1)))
print(npc.identity(-1))

print("\nGithub tests:")
print(npc.from_list([[],[]]),npc.from_list([[],[]]).shape, npc.from_list([[],[]]).dtype)
print("")
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6]]))
print("")
print(npc.from_tuple(("a","b","c")), npc.from_tuple(("a","b","c")).dtype)
print("")
print(npc.from_iterable(range(5)))
print("")
print(npc.from_shape((0, 0)), npc.from_shape((0, 0)).shape, npc.from_shape((0, 0)).dtype)
print("")
print(npc.from_shape((3, 5)))
print("")
print(npc.random((3, 5)))
print("")
print(npc.identity(4))
