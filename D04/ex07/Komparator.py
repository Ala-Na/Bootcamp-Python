
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class Komparator():

    def __init__(self, df):
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        comp_cat = self.df[categorical_var].unique()
        to_replace = {}
        for i in range(len(comp_cat)):
            to_replace[i] = comp_cat[i]
        df = self.df.drop_duplicates(subset=['ID'])
        df.loc[categorical_var] = df[categorical_var].replace(to_replace=to_replace)
        legend = comp_cat.tolist()
        sns.boxplot(x=categorical_var, y=numerical_var,data=df, order=legend)
        plt.show()

    def density(self, categorical_var, numerical_var):
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            sns.kdeplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(), label=elem)
        plt.legend()
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        self.df.hist(column=numerical_var, by=categorical_var)
        plt.show()