from data.data import HOTSPOTS


class Second_task():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def get_count_hotspots_with_place(self) -> int:
        hotspots_google_place = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id][HOTSPOTS.google_place_id.notnull()][HOTSPOTS.foursquare_id.isnull()].count()
        hotspots_foursquare = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id][HOTSPOTS.foursquare_id.notnull()][HOTSPOTS.google_place_id.isnull()].count()
        hotspots_places = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id][HOTSPOTS.foursquare_id.notnull()][HOTSPOTS.google_place_id.notnull()].count()
        all_hotspots = hotspots_google_place + hotspots_foursquare + hotspots_places
        return all_hotspots
