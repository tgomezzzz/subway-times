import requests
import gtfs_realtime_pb2 as gtfs
import datetime as dt

# 1, 2, 3, 4, 5, 6, 7 trains
url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
KEY_PATH = '../key.txt'
STATIONS_PATH = '../data/stops.txt'

def getKey():
    try:
        f = open(KEY_PATH, 'r')
        key = f.read()
        f.close()
        return key
    except:
        raise Exception("Unable to find MTA API key")

def getStations():
    try:
        f = open(STATIONS_PATH, 'r')
        f.readline()
        stations = {}
        for line in f:
            data = line.split(',')
            if len(data) > 0 and data[0] != '' and data[2] != '':
                stations[data[0]] = data[2]
        f.close()
        return stations
    except:
        print("Unable to read stations")
        return {}

def main():
    resp = requests.get(url, headers={'x-api-key': getKey()})
    stations = getStations()

    train_info = gtfs.FeedMessage()
    train_info.ParseFromString(resp.content)
    
    for entity in train_info.entity:
        if entity.HasField('trip_update'):
            trip_update = entity.trip_update
            if trip_update.HasField('trip'):
                trip = trip_update.trip
                if trip.HasField('route_id') and trip.route_id == "1":
                    for update in trip_update.stop_time_update:
                        if update.HasField('stop_id') and update.stop_id == "117N":
                            if update.HasField('arrival') and update.arrival.HasField('time'):
                                time = dt.datetime.fromtimestamp(update.arrival.time)
                                print("Found Northbound 1 train arriving at", time)
                        elif update.HasField('stop_id') and update.stop_id == "117S":
                            if update.HasField('arrival') and update.arrival.HasField('time'):
                                time = dt.datetime.fromtimestamp(update.arrival.time)
                                print("Found Southbound 1 train arriving at", time)

if __name__ == '__main__':
    main()
