import pandas as pd

def youngestfellah(df, year):
    if not isinstance(df, pd.DataFrame) or not (isinstance(year, str) or isinstance(year, int)):
        return None
    year_selection = df.loc[df['Year'] == year]
    men = year_selection.loc[year_selection['Sex'] == 'M']
    women = year_selection.loc[year_selection['Sex'] == 'F']
    youngest_woman = women.nsmallest(1, 'Age')
    youngest_man = men.nsmallest(1, 'Age')
    try:
        f_value = youngest_woman.iloc[0]['Age']
    except:
        f_value = 'nan'
    try:
        m_value = youngest_man.iloc[0]['Age']
    except:
        m_value = 'nan'
    dic = {'f' : f_value, 'm' : m_value}
    return dic
