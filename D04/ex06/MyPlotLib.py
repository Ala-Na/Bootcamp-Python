import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class   MyPlotLib():

    def histogram(self, data, features):
        values = pd.DataFrame(data[features])
        values.hist()
        plt.show()

    def density(self, data, features):
        values = pd.DataFrame(data[features])
        values.plot.density()
        plt.show()

    def pair_plot(self, data, features):
        sns.pairplot(data[features])
        plt.show()

    def box_plot(self, data, features):
        values = pd.DataFrame(data[features])
        values.boxplot()
        plt.show()