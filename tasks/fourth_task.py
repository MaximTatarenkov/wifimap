from collections import namedtuple

from data.data import CsvLoader


class FourthTask():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def get_hotspots_quality(self):
        hotspots = CsvLoader.load("hotspots")
        good_hotspots = hotspots.id[hotspots.owner_id == self.client_id][hotspots.score_v4 > 0.6].count()
        medium_hotspots = hotspots.id[hotspots.owner_id == self.client_id][hotspots.score_v4 < 0.6][hotspots.score_v4 > 0.3].count()
        bad_hotspots = hotspots.id[hotspots.owner_id == self.client_id][hotspots.score_v4 < 0.3].count()
        Hotspot = namedtuple("Hotspot", "good medium bad")
        result = Hotspot(good_hotspots, medium_hotspots, bad_hotspots)
        return result


if __name__=="__main__":
    pass
