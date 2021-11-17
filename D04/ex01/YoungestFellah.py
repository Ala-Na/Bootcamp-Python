import pandas as pd
import pandas.DataFrame as df

def youngestfellah(df, year):
    year_selection = df.loc[df['Year'] == year]
    mens = df.loc[year_selection['Sex'] == 'M']
    womens = df.loc[year_selection['Sex'] == 'F']
    youngest_woman = womens.nsmallest(1, 'Age')
    youngest_man = mens.nsmallest(1, 'Age')
    dic = {'f' : womens.iloc('Age'), 'm' : mens.iloc('Age')}
    return dic