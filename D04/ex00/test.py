from FileLoader import FileLoader
loader = FileLoader()
data = loader.load("../athlete_events.csv")
loader.display(data, 0)
loader.display(data, 12)
loader.display(data, 3)
loader.display(data, -3)

print("\nErrors:")
loader.display(data, 'lol')
data = loader.load("non_existing.csv")
loader.display(data, 1)
print("Nothing should be output")
