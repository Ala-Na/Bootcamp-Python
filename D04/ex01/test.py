from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
from YoungestFellah import youngestfellah
youngestfellah(data, 2004)