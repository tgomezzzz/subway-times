import requests
import gtfs_realtime_pb2 as gtfs

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

    proto = gtfs.FeedMessage()
    proto.ParseFromString(resp.content)
    print(stations)

if __name__ == '__main__':
    main()
