from collections import namedtuple

from data.data import CsvLoader
from .first_task import FirstTask


class FourthTask(FirstTask):

    def get_hotspots_quality(self):
        hotspots = CsvLoader.load(self.hotspots_file)
        good_hotspots = hotspots.id[hotspots.owner_id == self.client_id][hotspots.score_v4 > 0.6].count()
        medium_hotspots = hotspots.id[hotspots.owner_id == self.client_id][hotspots.score_v4 < 0.6][hotspots.score_v4 > 0.3].count()
        bad_hotspots = hotspots.id[hotspots.owner_id == self.client_id][hotspots.score_v4 < 0.3].count()
        Hotspot = namedtuple("Hotspot", "good medium bad")
        result = Hotspot(good_hotspots, medium_hotspots, bad_hotspots)
        return result


if __name__=="__main__":
    pass
