import pandas as pd


class CsvLoader():

    @staticmethod
    def load(filename):

        match filename:
            case "users":
                file_csv = pd.read_csv("./data/users_test.csv")
            case "hotspots":
                file_csv = pd.read_csv("./data/hotspots_test.csv")
            case "conns":
                file_csv = pd.read_csv("./data/conns_test.csv")
            case _:
                file_csv = pd.read_csv(filename)
        return file_csv

if __name__=="__main__":
    pass
