from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from ProportionBySport import proportionBySport

print("\nToo fit subject with dropping duplicates (logic):")

print(proportionBySport(data, 2004, 'Tennis', 'F'), end = "\n\n")
print(proportionBySport(data, 2008, 'Hockey', 'F'), end = "\n\n")
print(proportionBySport(data, 1964, 'Biathlon', 'M'), end = "\n\n")

# DO NOT TAKE CORRECTION VALUES INTO ACCOUNT
# https://github.com/42-AI/Python-Bootcamp-Corrections/issues/9

print("\nWithout dropping duplicates as correction:")

from ProportionBySport import proportionBySportCorrection
print(proportionBySportCorrection(data, 2004, 'Tennis', 'F'), end = "\n\n")
print(proportionBySportCorrection(data, 2008, 'Hockey', 'F'), end = "\n\n")
print(proportionBySportCorrection(data, 1964, 'Biathlon', 'M'), end = "\n\n")
