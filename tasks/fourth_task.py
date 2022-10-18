from collections import namedtuple

from data.data import HOTSPOTS


class Fourth_task():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def get_hotspots_quality(self):
        good_hotspots = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id][HOTSPOTS.score_v4 > 0.6].count()
        medium_hotspots = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id][HOTSPOTS.score_v4 < 0.6][HOTSPOTS.score_v4 > 0.3].count()
        bad_hotspots = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id][HOTSPOTS.score_v4 < 0.3].count()
        Hotspot = namedtuple("Hotspot", "good medium bad")
        result = Hotspot(good_hotspots, medium_hotspots, bad_hotspots)
        return result
