from data.data import CsvLoader


class FirstTask():

    def __init__(self, client_id, hotspots_file) -> None:
        self.client_id = client_id
        self.hotspots_file = hotspots_file

    def get_hotspots(self) -> int:
        hotspots = CsvLoader.load(self.hotspots_file)
        client_hotspots = hotspots.id[hotspots.owner_id == self.client_id].count()
        return client_hotspots


if __name__=="__main__":
    pass
