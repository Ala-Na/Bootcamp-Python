from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from MyPlotLib import MyPlotLib
myplot = MyPlotLib()

myplot.histogram(data, ['Height'])
myplot.histogram(data, ['Height', 'Weight'])
print("Team can't be shown as data")
myplot.histogram(data, ['Height', 'Weight', 'Team'])
myplot.histogram(data, ['Height', 'Weight', 'Age'])

myplot.density(data, ['Height'])
myplot.density(data, ['Height', 'Weight'])
print("Team can't be shown as data")
myplot.density(data, ['Height', 'Weight', 'Team'])
myplot.density(data, ['Height', 'Weight', 'Age'])

myplot.pair_plot(data, ['Height'])
myplot.pair_plot(data, ['Height', 'Weight'])
print("Team can't be shown as data")
myplot.pair_plot(data, ['Height', 'Weight', 'Team'])
myplot.pair_plot(data, ['Height', 'Weight', 'Age'])

myplot.box_plot(data, ['Height'])
myplot.box_plot(data, ['Height', 'Weight'])
print("Team can't be shown as data")
myplot.box_plot(data, ['Height', 'Weight', 'Team'])
myplot.box_plot(data, ['Height', 'Weight', 'Age'])
