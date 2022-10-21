from data.data import CsvLoader
from .first_task import FirstTask


class SecondTask(FirstTask):

    def get_count_hotspots_with_place(self) -> int:
        hotspots = CsvLoader.load(self.hotspots_file)
        hotspots_google_place = hotspots.id[hotspots.owner_id == self.client_id][hotspots.google_place_id.notnull()][hotspots.foursquare_id.isnull()].count()
        hotspots_foursquare = hotspots.id[hotspots.owner_id == self.client_id][hotspots.foursquare_id.notnull()][hotspots.google_place_id.isnull()].count()
        hotspots_places = hotspots.id[hotspots.owner_id == self.client_id][hotspots.foursquare_id.notnull()][hotspots.google_place_id.notnull()].count()
        all_hotspots = hotspots_google_place + hotspots_foursquare + hotspots_places
        return all_hotspots


if __name__=="__main__":
    pass
