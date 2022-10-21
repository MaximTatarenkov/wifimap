from tasks.first_task import FirstTask
from tasks.second_task import SecondTask
from tasks.third_task import ThirdTask
from tasks.fourth_task import FourthTask
from tasks.fifth_task import FifthTask


if __name__=="__main__":
    client_id = 221322
    first_task = FirstTask(client_id)
    hotspots = first_task.get_hotspots()
    print(f"Пользователь создал WiFi точек: {hotspots}")

    second_task = SecondTask(client_id)
    hotspots_with_place = second_task.get_count_hotspots_with_place()
    print(f"WiFi точек с привязкой к месту: {hotspots_with_place}")

    third_task = ThirdTask(client_id)
    hotposts_count = third_task.get_hotposts_last_month_week()
    last_month_hotposts_count = hotposts_count.last_month
    last_week_hotposts_count = hotposts_count.last_week
    print(f"Создано WiFi точек за последний месяц: {last_month_hotposts_count}")
    print(f"Создано WiFi точек за последнюю неделю: {last_week_hotposts_count}")

    fourth_task = FourthTask(client_id)
    hotposts_count = fourth_task.get_hotspots_quality()
    good_hotposts = hotposts_count.good
    medium_hotposts = hotposts_count.medium
    bad_hotposts = hotposts_count.bad
    print(f"Хороших WiFi точек: {good_hotposts}")
    print(f"Средних WiFi точек: {medium_hotposts}")
    print(f"Плохих WiFi точек: {bad_hotposts}")

    fifth_task = FifthTask(client_id)
    conns_count = fifth_task.get_unique_conns()
    all_time_conns = conns_count.all_time
    year_conns = conns_count.year
    month_conns = conns_count.month
    week_conns = conns_count.week
    print("Подключений за все время:")
    print(f"Более десяти: {all_time_conns['over_ten']}, более пяти: {all_time_conns['over_five']}, более одного: {all_time_conns['over_one']}")
    print("Подключений за последний год:")
    print(f"Более десяти: {year_conns['over_ten']}, более пяти: {year_conns['over_five']}, более одного: {year_conns['over_one']}")
    print("Подключений за последний месяц:")
    print(f"Более десяти: {month_conns['over_ten']}, более пяти: {month_conns['over_five']}, более одного: {month_conns['over_one']}")
    print("Подключений за последнюю неделю:")
    print(f"Более десяти: {week_conns['over_ten']}, более пяти: {week_conns['over_five']}, более одного: {week_conns['over_one']}")
