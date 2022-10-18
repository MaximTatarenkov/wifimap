from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import namedtuple

from data.data import HOTSPOTS

DATE_WITHOUT_LAST_YEAR = datetime.now() - relativedelta(years=1)
DATE_WITHOUT_LAST_MONTH = datetime.now() - relativedelta(months=1)
DATE_WITHOUT_LAST_WEEK = datetime.now() - timedelta(weeks=1)


class Third_task():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def replace_string_to_date(cls, date) -> datetime:
        replaced_date = date.replace("T", " ").split(".")[0]
        dt_date = datetime.strptime(replaced_date, "%Y-%m-%d %H:%M:%S")
        return dt_date

    def get_hotposts_last_month_week(self):
        last_month_hotposts_count = 0
        last_week_hotposts_count = 0
        for spot in HOTSPOTS.itertuples():
            if spot.created_at != " ":
                HOTSPOTS.loc[spot.Index, "created_at"] = self.replace_string_to_date(spot.created_at)
                if spot.owner_id == self.client_id:
                    if HOTSPOTS.loc[spot.Index, "created_at"] >= DATE_WITHOUT_LAST_MONTH:
                        last_month_hotposts_count += 1
                    if HOTSPOTS.loc[spot.Index, "created_at"] >= DATE_WITHOUT_LAST_WEEK:
                        last_week_hotposts_count += 1
        Hotspot = namedtuple("Hotspot", "last_month last_week")
        result = Hotspot(last_month_hotposts_count, last_week_hotposts_count)
        return result
