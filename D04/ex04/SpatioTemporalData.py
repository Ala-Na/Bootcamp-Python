
from numpy import isin
import pandas as pd

class SpatioTemporalData():

    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError()
        self.df = df

    def when(self, location):
        if not isinstance(location, str):
            return None
        in_location = self.df.loc[self.df['City'] == location].drop_duplicates(subset='Year')
        return in_location['Year'].to_list()

    def where(self, date):
        if not (isinstance(date, str) or isinstance(date, int)):
            return None
        in_location = self.df.loc[self.df['Year'] == date].drop_duplicates(subset='City')
        return in_location['City'].to_list()
