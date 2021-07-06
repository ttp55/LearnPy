# @Time : 2021/6/29 13:52
# @Author : WZG
# --coding:utf-8--

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # 你传入一个数组，它被转换为集合

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()


while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_stations in stations.items():
        covered = states_needed & states_for_stations
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)
print(final_stations)