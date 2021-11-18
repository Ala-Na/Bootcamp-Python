from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from MyPlotLib import MyPlotLib
myplot = MyPlotLib()

myplot.box_plot(data, ['Height', 'Weight', 'Team'])