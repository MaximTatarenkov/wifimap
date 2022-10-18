from tasks.first_task import First_task
from tasks.second_task import Second_task
from tasks.third_task import Third_task
from tasks.fourth_task import Fourth_task
from tasks.fifth_task import Fifth_task


if __name__=="__main__":
    client_id = 221322
    first_task = First_task(client_id)
    hotspots = first_task.get_hotspots()
    print(hotspots)

    second_task = Second_task(client_id)
    hotspots_with_place = second_task.get_count_hotspots_with_place()
    print(hotspots_with_place)

    third_task = Third_task(client_id)
    hotposts_count = third_task.get_hotposts_last_month_week()
    last_month_hotposts_count = hotposts_count.last_month
    last_week_hotposts_count = hotposts_count.last_week
    print(last_month_hotposts_count)
    print(last_week_hotposts_count)

    fourth_task = Fourth_task(client_id)
    hotposts_count = fourth_task.get_hotspots_quality()
    good_hotposts = hotposts_count.good
    medium_hotposts = hotposts_count.medium
    bad_hotposts = hotposts_count.bad
    print(good_hotposts)
    print(medium_hotposts)
    print(bad_hotposts)

    fifth_task = Fifth_task(client_id)
    conns_count = fifth_task.get_unique_conns()
    over_ten_conns = conns_count.ten_conns
    over_five_conns = conns_count.five_conns
    over_one_conns = conns_count.one_conns
    print(over_ten_conns)
    print(over_five_conns)
    print(over_one_conns)
