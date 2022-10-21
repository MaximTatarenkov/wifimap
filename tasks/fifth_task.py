from datetime import datetime
from collections import namedtuple

from data.data import CsvLoader
from .third_task import DATE_WITHOUT_LAST_YEAR, DATE_WITHOUT_LAST_MONTH, DATE_WITHOUT_LAST_WEEK
from .first_task import FirstTask


class FifthTask(FirstTask):

    def __init__(self, client_id, hotspots_file, conns_file) -> None:
        super().__init__(client_id, hotspots_file)
        self.conns_file = conns_file


    def get_conns_count(self, hotposts):
        conns_count = {"over_one": 0, "over_five": 0, "over_ten": 0}
        for hotpost in hotposts:
            if 5 > hotposts[hotpost] >= 1:
                conns_count["over_one"] += 1
            elif 10 > hotposts[hotpost] >= 5:
                conns_count["over_one"] += 1
                conns_count["over_five"] += 1
            elif hotposts[hotpost] >= 10:
                conns_count["over_one"] += 1
                conns_count["over_five"] += 1
                conns_count["over_ten"] += 1
        return conns_count


    def get_unique_conns(self):
        hotspots = CsvLoader.load(self.hotspots_file)
        conns = CsvLoader.load(self.conns_file)
        client_hotspots = hotspots.id[hotspots.owner_id == self.client_id]
        unique_client_cons = []
        unique_client_cons_with_date = []

        for hotspot in client_hotspots:
            client_conns = conns[["installation_id", "connected_at", "hotspot_id"]][conns.hotspot_id == hotspot]
            for conn in client_conns.itertuples():
                if conn.installation_id not in unique_client_cons:
                    unique_client_cons.append(conn.installation_id)
                    unique_client_cons_with_date.append([conn.installation_id, conn.connected_at, conn.hotspot_id])

        hotposts_all_time = {}
        hotposts_year = {}
        hotposts_month = {}
        hotposts_week = {}
        for conn in unique_client_cons_with_date:
            if "." in conn[1]:
                conn[1] = datetime.strptime(conn[1], "%Y-%m-%d %H:%M:%S.%f")
            else:
                conn[1] = datetime.strptime(conn[1], "%Y-%m-%d %H:%M:%S")
            if conn[2] not in hotposts_all_time:
                hotposts_all_time[conn[2]] = 1
            else:
                hotposts_all_time[conn[2]] += 1
            if conn[1] >= DATE_WITHOUT_LAST_WEEK:
                if conn[2] not in hotposts_week:
                    hotposts_week[conn[2]] = 1
                else:
                    hotposts_week[conn[2]] += 1
            if conn[1] >= DATE_WITHOUT_LAST_MONTH:
                if conn[2] not in hotposts_month:
                    hotposts_month[conn[2]] = 1
                else:
                    hotposts_month[conn[2]] += 1
            if conn[1] >= DATE_WITHOUT_LAST_YEAR:
                if conn[2] not in hotposts_year:
                    hotposts_year[conn[2]] = 1
                else:
                    hotposts_year[conn[2]] += 1

        conns_count_all_time = self.get_conns_count(hotposts_all_time)
        conns_count_year = self.get_conns_count(hotposts_year)
        conns_count_month = self.get_conns_count(hotposts_month)
        conns_count_week = self.get_conns_count(hotposts_week)
        Conn = namedtuple("Conn", "all_time year month week")
        result = Conn(conns_count_all_time, conns_count_year, conns_count_month, conns_count_week)
        return result


if __name__=="__main__":
    pass
