from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from HowManyMedals import howManyMedals
print(howManyMedals(data, 'Kjetil Andr Aamodt'), end="\n\n")
print(howManyMedals(data, 'Gary Abraham'), end="\n\n")
print(howManyMedals(data, 'Yekaterina Konstantinovna Abramova'), end="\n\n")
print(howManyMedals(data, 'Kristin Otto'), end="\n\n")
