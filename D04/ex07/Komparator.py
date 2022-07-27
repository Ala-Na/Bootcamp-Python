
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Komparator():

    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Komparator didn't receive a dataframe in constructor.")
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            return None
        # # One boxplot will be made per categorical_var because of 'by'
        # self.df.boxplot(column=[numerical_var], by=categorical_var)
        # plt.show()
        try:
            comp_cat = self.df[categorical_var].unique()
            to_replace = {}
            for i in range(len(comp_cat)):
                to_replace[i] = comp_cat[i]
            df = self.df.drop_duplicates(subset=['ID'])
            df.loc[categorical_var] = df[categorical_var].replace(to_replace=to_replace)
            legend = comp_cat.tolist()
            legend = [x for x in legend if str(x) != 'nan']
            sns.boxplot(x=categorical_var, y=numerical_var, data=df, order=legend)
            plt.show()
        except:
            print("Something went wrong")

    def density(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            return None
        try:
            for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
                sns.kdeplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(), label=elem)
            plt.legend()
            plt.show()
        except:
            print("Something went wrong")

    def compare_histograms(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            return None
        try:
            self.df.hist(column=numerical_var, by=categorical_var)
            plt.show()
        except:
            print("Something went wrong")
