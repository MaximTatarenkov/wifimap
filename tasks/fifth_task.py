from datetime import datetime
from collections import namedtuple

from data.data import HOTSPOTS, CONNS
from .third_task import DATE_WITHOUT_LAST_YEAR, DATE_WITHOUT_LAST_MONTH, DATE_WITHOUT_LAST_WEEK


class Fifth_task():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def get_unique_conns(self):
        client_hotspots = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id]
        unique_client_cons = []
        unique_client_cons_with_date = []

        for hotspot in client_hotspots:
            client_conns = CONNS[["installation_id", "connected_at", "hotspot_id"]][CONNS.hotspot_id == hotspot]
            for conn in client_conns.itertuples():
                # print(conn.installation_id)
                if conn.installation_id not in unique_client_cons:
                    unique_client_cons.append(conn.installation_id)
                    unique_client_cons_with_date.append([conn.installation_id, conn.connected_at, conn.hotspot_id])

        hotposts_for_conns_all_time = {}
        hotposts_for_conns_year = {}
        hotposts_for_conns_month = {}
        hotposts_for_conns_week = {}
        for conn in unique_client_cons_with_date:
            if "." in conn[1]:
                conn[1] = datetime.strptime(conn[1], "%Y-%m-%d %H:%M:%S.%f")
            else:
                conn[1] = datetime.strptime(conn[1], "%Y-%m-%d %H:%M:%S")
            if conn[2] not in hotposts_for_conns_all_time:
                hotposts_for_conns_all_time[conn[2]] = 1
            else:
                hotposts_for_conns_all_time[conn[2]] += 1
            if conn[1] >= DATE_WITHOUT_LAST_WEEK:
                if conn[2] not in hotposts_for_conns_week:
                    hotposts_for_conns_week[conn[2]] = 1
                else:
                    hotposts_for_conns_week[conn[2]] += 1
            if conn[1] >= DATE_WITHOUT_LAST_MONTH:
                if conn[2] not in hotposts_for_conns_month:
                    hotposts_for_conns_month[conn[2]] = 1
                else:
                    hotposts_for_conns_month[conn[2]] += 1
            if conn[1] >= DATE_WITHOUT_LAST_YEAR:
                if conn[2] not in hotposts_for_conns_year:
                    hotposts_for_conns_year[conn[2]] = 1
                else:
                    hotposts_for_conns_year[conn[2]] += 1

        over_one_conns = {"all_time": 0, "year": 0, "month": 0, "week": 0}
        over_five_conns ={"all_time": 0, "year": 0, "month": 0, "week": 0}
        over_ten_conns = {"all_time": 0, "year": 0, "month": 0, "week": 0}

        for hotpost in hotposts_for_conns_all_time:
            if 5 > hotposts_for_conns_all_time[hotpost] >= 1:
                over_one_conns["all_time"] += 1
            elif 10 > hotposts_for_conns_all_time[hotpost] >= 5:
                over_one_conns["all_time"] += 1
                over_five_conns["all_time"] += 1
            elif hotposts_for_conns_all_time[hotpost] >= 10:
                over_ten_conns["all_time"] += 1
                over_five_conns["all_time"] += 1
                over_one_conns["all_time"] += 1

        for hotpost in hotposts_for_conns_year:
            if 5 > hotposts_for_conns_year[hotpost] >= 1:
                over_one_conns["year"] += 1
            elif 10 > hotposts_for_conns_year[hotpost] >= 5:
                over_one_conns["year"] += 1
                over_five_conns["year"] += 1
            elif hotposts_for_conns_year[hotpost] >= 10:
                over_ten_conns["year"] += 1
                over_five_conns["year"] += 1
                over_one_conns["year"] += 1

        for hotpost in hotposts_for_conns_month:
            if 5 > hotposts_for_conns_month[hotpost] >= 1:
                over_one_conns["month"] += 1
            elif 10 > hotposts_for_conns_month[hotpost] >= 5:
                over_one_conns["month"] += 1
                over_five_conns["month"] += 1
            elif hotposts_for_conns_month[hotpost] >= 10:
                over_ten_conns["month"] += 1
                over_five_conns["month"] += 1
                over_one_conns["month"] += 1

        for hotpost in hotposts_for_conns_week:
            if 5 > hotposts_for_conns_week[hotpost] >= 1:
                over_one_conns["week"] += 1
            elif 10 > hotposts_for_conns_week[hotpost] >= 5:
                over_one_conns["week"] += 1
                over_five_conns["week"] += 1
            elif hotposts_for_conns_week[hotpost] >= 10:
                over_ten_conns["week"] += 1
                over_five_conns["week"] += 1
                over_one_conns["week"] += 1
        Conn = namedtuple("Conn", "ten_conns five_conns one_conns")
        result = Conn(over_ten_conns, over_five_conns, over_one_conns)
        return result
