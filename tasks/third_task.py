from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import namedtuple

from data.data import CsvLoader
from .first_task import FirstTask

DATE_WITHOUT_LAST_YEAR = datetime.now() - relativedelta(years=1)
DATE_WITHOUT_LAST_MONTH = datetime.now() - relativedelta(months=1)
DATE_WITHOUT_LAST_WEEK = datetime.now() - timedelta(weeks=1)


class ThirdTask(FirstTask):

    def replace_string_to_date(cls, date) -> datetime:
        replaced_date = date.replace("T", " ").split(".")[0]
        dt_date = datetime.strptime(replaced_date, "%Y-%m-%d %H:%M:%S")
        return dt_date

    def get_hotposts_last_month_week(self):
        last_month_hotposts_count = 0
        last_week_hotposts_count = 0
        hotspots = CsvLoader.load(self.hotspots_file)
        for spot in hotspots.itertuples():
            if spot.created_at != " ":
                hotspots.loc[spot.Index, "created_at"] = self.replace_string_to_date(spot.created_at)
                if spot.owner_id == self.client_id:
                    if hotspots.loc[spot.Index, "created_at"] >= DATE_WITHOUT_LAST_MONTH:
                        last_month_hotposts_count += 1
                    if hotspots.loc[spot.Index, "created_at"] >= DATE_WITHOUT_LAST_WEEK:
                        last_week_hotposts_count += 1
        Hotspot = namedtuple("Hotspot", "last_month last_week")
        result = Hotspot(last_month_hotposts_count, last_week_hotposts_count)
        return result


if __name__=="__main__":
    pass
