from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')

from SpatioTemporalData import SpatioTemporalData
sp = SpatioTemporalData(data)

print(sp.where(1896))

print(sp.where(2016))

print(sp.when('Athina'))

print(sp.when('Paris'))

print(sp.where(2000))

print(sp.where(1980))

print(sp.when('London'))
