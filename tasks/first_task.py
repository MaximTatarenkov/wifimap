from data.data import CsvLoader


class FirstTask():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def get_hotspots(self) -> int:
        hotspots = CsvLoader.load("hotspots")
        client_hotspots = hotspots.id[hotspots.owner_id == self.client_id].count()
        return client_hotspots


if __name__=="__main__":
    pass
