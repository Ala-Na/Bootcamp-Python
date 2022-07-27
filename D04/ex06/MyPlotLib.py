import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class   MyPlotLib():

    def histogram(self, data, features):
        try:
            values = pd.DataFrame(data[features])
            values.hist()
            plt.show()
        except:
            print("Something went wrong")

    def density(self, data, features):
        try:
            values = pd.DataFrame(data[features])
            values.plot.density()
            plt.show()
        except:
            print("Something went wrong")

    def pair_plot(self, data, features):
        try:
            sns.pairplot(data[features])
            plt.show()
        except:
            print("Something went wrong")

    def box_plot(self, data, features):
        try:
            values = pd.DataFrame(data[features])
            values.boxplot()
            plt.show()
        except:
            print("Something went wrong")

