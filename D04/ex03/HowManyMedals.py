import pandas as pd
from collections import OrderedDict

def howManyMedals(df, participant):
    if not isinstance(df, pd.DataFrame) or not isinstance(participant, str):
        return None
    for_paticipant = df.loc[df['Name'] == participant]
    group_by_year = for_paticipant[['Year', 'Medal']].value_counts(dropna=False)
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
        if not pd.isna(index[1]):
            medals[index[0]][index[1][0]] = res
    return medals
