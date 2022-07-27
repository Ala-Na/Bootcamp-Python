import pandas as pd
import os

class FileLoader:

    def load(self, path):
        if not os.path.isfile(path):
            return None
        try:
            datas = pd.read_csv(path)
            print("Loading dataset of dimensions {} x {}".format(datas.shape[0], datas.shape[1]))
            return datas
        except:
            return None

    def display(self, df, n):
        if not isinstance(df, pd.DataFrame):
            return None
        if not isinstance(n, int):
            return None
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
