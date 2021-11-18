from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from ProportionBySport import proportionBySport
print(proportionBySport(data, 2004, 'Tennis', 'F'))