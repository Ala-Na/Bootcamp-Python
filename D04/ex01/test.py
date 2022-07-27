from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../athlete_events.csv')

from YoungestFellah import youngestfellah
print('2004: ', youngestfellah(data, 2004))
print('1992: ', youngestfellah(data, 1992))
print('2010: ', youngestfellah(data, 2010))
print('1991: ', youngestfellah(data, 1991))
print('1912: ', youngestfellah(data, 1912))
print('2003: ', youngestfellah(data, 2003))
print('2103: ', youngestfellah(data, 2103))
