import requests
import gtfs_realtime_pb2 as gtfs

# 1, 2, 3, 4, 5, 6, 7
url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
KEYPATH = '../key.txt'

def getKey():
    try:
        f = open(KEYPATH, 'r')
        key = f.read()
        f.close()
        return key
    except:
        raise Exception("Unable to find MTA API key")

def main():
    resp = requests.get(url, headers={'x-api-key': getKey()})

    proto = gtfs.FeedMessage()
    proto.ParseFromString(resp.content)
    print(proto)

if __name__ == '__main__':
    main()
