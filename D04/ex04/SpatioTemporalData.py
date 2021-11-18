
class SpatioTemporalData():

    def __init__(self, df):
        self.df = df

    def when(self, location):
        in_location = self.df.loc[self.df['City'] == location].drop_duplicates(subset='Year')
        return in_location['Year'].to_list()

    def where(self, date):
        in_location = self.df.loc[self.df['Year'] == date].drop_duplicates(subset='City')
        return in_location['City'].to_list()
