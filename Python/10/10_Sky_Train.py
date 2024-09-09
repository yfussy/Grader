def nextStation(linkedStation, start):
    stations = []
    for station in linkedStation:
        if start in station:
            nextStation = station[(station.index(start)+1)%2]
            if station not in stations:
                stations.append(nextStation)
    return stations

linked = []
while True:
    stations = sorted(input().split())
    if len(stations) == 1:
        start = stations[0]
        avaliableStations = nextStation(linked, start) + [start]
        for station in nextStation(linked, start):
            avaliableStations += nextStation(linked, station)
        avaliableStations = sorted(list(set(avaliableStations)))
        for station in avaliableStations:
            print(station)
        break
    if stations not in linked:
        linked.append(stations)