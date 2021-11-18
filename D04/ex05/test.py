from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from HowManyMedalsByCountry import howManyMedalsByCountry
print(howManyMedalsByCountry(data, 'China'))