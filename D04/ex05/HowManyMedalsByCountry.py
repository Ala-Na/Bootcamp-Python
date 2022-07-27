import pandas as pd

def howManyMedalsByCountry(df, country):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing',
                'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh',
                'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball',
                'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

    for_country = df[df.Team == country]
    teamsp = for_country[for_country.Sport.isin(team_sports)]
    teamsp = teamsp.drop_duplicates(['Event', 'Year', 'Medal'])
    nonteamsp = for_country[~for_country['Sport'].isin(team_sports)]
    all_sports = pd.concat([teamsp, nonteamsp])
    group_by_year = all_sports[['Year', 'Medal']].value_counts()

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
