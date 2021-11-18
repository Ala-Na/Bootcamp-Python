import pandas as pd

def howManyMedalsByCountry(df, country):
    for_country = df.loc[df['Team'] == country].drop_duplicates(['Event', 'Sport', 'Year', 'Games', 'Medal'])
    group_by_year = for_country[['Year', 'Medal']].value_counts()
    years_key = []
    for index, res in group_by_year.iteritems():
        if index[0] not in years_key:
            years_key.append(index[0])
    years_key.sort()
    medals = {}
    for key in years_key:
        medals[key] = {}
        medals[key]['G'] = 0
        medals[key]['S'] = 0
        medals[key]['B'] = 0
    for index, res in group_by_year.iteritems():
        medals[index[0]][index[1][0]] = res
    return medals