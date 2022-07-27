from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from MyPlotLib import MyPlotLib
myplot = MyPlotLib()
from Komparator import Komparator
komp = Komparator(data)
komp.compare_box_plots('Sex','Height')
komp.density('Sex','Height')
komp.compare_histograms('Sex', 'Height')

komp.compare_box_plots('Medal','Age')
komp.compare_histograms('Medal', 'Height')
komp.density('Medal','Weight')
