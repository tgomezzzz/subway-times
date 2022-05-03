import requests
import gtfs_realtime_pb2 as gtfs
from datetime import datetime as dt
from graphics import *

KEY_PATH = '../key.txt'
STATIONS_PATH = '../data/stops.txt'
BASE_URL = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
URL_SUFFIX = {
	'1': '',
	'2': '',
	'3': '',
	'4': '',
	'5': '',
	'6': '',
	'7': '',
	'A': '-ace',
	'C': '-ace',
	'E': '-ace',
	'N': '-nqrw',
	'Q': '-nqrw',
	'R': '-nqrw',
	'W': '-nqrw',
	'B': '-bdfm',
	'D': '-bdfm',
	'F': '-bdfm',
	'M': '-bdfm',
	'L': '-l',
	'J': '-jz',
	'Z': '-jz',
	'G': '-g'
}

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

KEY = getKey()
STATIONS = getStations()

class StopData:
	def __init__(self, id):
		self.id = id
		self.uptownData = []
		self.downtownData = []
	
	def addUptownData(self, stop):
		minutes = int(stop.total_seconds()/60)
		if minutes < 0:
			return
		self.uptownData.append(minutes)

	def addDowntownData(self, stop):
		minutes = int(stop.total_seconds()/60)
		if minutes < 0:
			return
		self.downtownData.append(minutes)

	def uptownTime(self, i):
		if i < len(self.uptownData):
			return self.uptownData[i]
		return -1

	def downtownTime(self, i):
		if i < len(self.downtownData):
			return self.downtownData[i]
		return -1

	def sort(self):
		self.uptownData.sort()
		self.downtownData.sort()

class Train:
	def __init__(self, id, center, r, color, win):
		self.id = id

		self.icon = Circle(center, r)
		self.icon.setFill(color)
		self.icon.setOutline("")

		self.text = Text(center, id)
		self.text.setFill("white")
		self.text.setSize(36)

		self.data = []
	
	def fetchData(self):
		url = BASE_URL + URL_SUFFIX[self.id]
		resp = requests.get(url, headers={'x-api-key': KEY})

		train_info = gtfs.FeedMessage()
		train_info.ParseFromString(resp.content)

		station_names = []
		station_ids = []
		station_data = {}

		for entity in train_info.entity:
			if entity.HasField('trip_update'):
				trip_update = entity.trip_update
				if trip_update.HasField('trip'):
					trip = trip_update.trip
					if trip.HasField('route_id') and trip.route_id == self.id:
						for update in trip_update.stop_time_update:
							if update.HasField('stop_id'):
								parent_id = update.stop_id[:3]
								if parent_id not in station_ids:
									station_ids.append(parent_id)
									if parent_id in STATIONS:
										station_names.append(STATIONS[parent_id])

								if parent_id not in STATIONS:
									continue

								if STATIONS[parent_id] not in station_data:
									station_data[STATIONS[parent_id]] = StopData(id)

								station = station_data[STATIONS[parent_id]]
								if update.HasField('arrival') and update.arrival.HasField('time'):
									direction = update.stop_id[-1]
									time = dt.fromtimestamp(update.arrival.time)
									if direction == 'N':
										station.addUptownData(time - dt.now())
									elif direction == 'S':
									   station.addDowntownData(time - dt.now()) 

		return station_names, station_data

	def draw(self, win):
		self.icon.draw(win)
		self.text.draw(win)

	def undraw(self):
		self.icon.undraw()
		self.text.undraw()

class Tr1(Train):
	def __init__(self, center, r, win):
		super().__init__("1", center, r, "red", win)

class Tr2(Train):
	def __init__(self, center, r, win):
		super().__init__("2", center, r, "red", win)

class Tr3(Train):
	def __init__(self, center, r, win):
		super().__init__("3", center, r, "red", win)

class Tr4(Train):
	def __init__(self, center, r, win):
		super().__init__("4", center, r, "green", win)

class Tr5(Train):
	def __init__(self, center, r, win):
		super().__init__("5", center, r, "green", win)

class Tr6(Train):
	def __init__(self, center, r, win):
		super().__init__("6", center, r, "green", win)

class Tr7(Train):
	def __init__(self, center, r, win):
		super().__init__("7", center, r, "purple", win)

class TrA(Train):
	def __init__(self, center, r, win):
		super().__init__("A", center, r, "blue", win)

class TrC(Train):
	def __init__(self, center, r, win):
		super().__init__("C", center, r, "blue", win)

class TrE(Train):
	def __init__(self, center, r, win):
		super().__init__("E", center, r, "blue", win)

class TrN(Train):
	def __init__(self, center, r, win):
		super().__init__("N", center, r, "yellow", win)
		self.text.setFill('black')

class TrQ(Train):
	def __init__(self, center, r, win):
		super().__init__("Q", center, r, "yellow", win)
		self.text.setFill('black')

class TrR(Train):
	def __init__(self, center, r, win):
		super().__init__("R", center, r, "yellow", win)
		self.text.setFill('black')

class TrW(Train):
	def __init__(self, center, r, win):
		super().__init__('W', center, r, "yellow", win)
		self.text.setFill('black')

class TrB(Train):
	def __init__(self, center, r, win):
		super().__init__("B", center, r, "orange", win)

class TrD(Train):
	def __init__(self, center, r, win):
		super().__init__("D", center, r, "orange", win)

class TrF(Train):
	def __init__(self, center, r, win):
		super().__init__("F", center, r, "orange", win)

class TrM(Train):
	def __init__(self, center, r, win):
		super().__init__("M", center, r, "orange", win)

class TrL(Train):
	def __init__(self, center, r, win):
		super().__init__("L", center, r, "grey", win)

class TrJ(Train):
	def __init__(self, center, r, win):
		super().__init__("J", center, r, color_rgb(139, 69, 19), win)

class TrZ(Train):
	def __init__(self, center, r, win):
		super().__init__("Z", center, r, color_rgb(139, 69, 19), win)

class TrG(Train):
	def __init__(self, center, r, win):
		super().__init__("G", center, r, color_rgb(96, 209, 98), win)