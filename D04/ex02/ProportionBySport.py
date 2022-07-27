import pandas as pd

def proportionBySport(df, year, sport, gender):
    if not isinstance(df, pd.DataFrame):
        return None
    by_year = df.loc[df['Year'] == year]
    by_gender = by_year.loc[by_year['Sex'] == gender].drop_duplicates(subset='ID')
    proportion_all_sports = by_gender['Sport'].value_counts(normalize=True)
    return proportion_all_sports[sport]

def proportionBySportCorrection(df, year, sport, gender):
    if not isinstance(df, pd.DataFrame):
        return None
    by_year = df.loc[df['Year'] == year]
    by_gender = by_year.loc[by_year['Sex'] == gender]
    proportion_all_sports = by_gender['Sport'].value_counts(normalize=True)
    return proportion_all_sports[sport]
