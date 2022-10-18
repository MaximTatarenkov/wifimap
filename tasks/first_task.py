from data.data import HOTSPOTS


class First_task():

    def __init__(self, client_id) -> None:
        self.client_id = client_id

    def get_hotspots(self) -> int:
        client_hotspots = HOTSPOTS.id[HOTSPOTS.owner_id == self.client_id].count()
        return client_hotspots


if __name__=="__main__":
    pass
