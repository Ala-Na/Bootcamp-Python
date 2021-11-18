from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../athlete_events.csv')

from YoungestFellah import youngestfellah
print(youngestfellah(data, 2004))
print(youngestfellah(data, 1991))
print(youngestfellah(data, 1912))