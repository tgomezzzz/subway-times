import serial

JOYSTICK_REST = 2000

class SerialReader:
	def __init__(self, port, baud, data):
		self.port = port
		self.baud = baud
		self.data = data
		self.ser = serial.Serial(port, baud)
		self.cooldown = 0

	def readLine(self):
		try:
			line = str(self.ser.readline().strip(), self.data)
			args = line.split(',')
			x = int(args[0])
			y = int(args[1])
			if x < 1000:
				return 'Left'
			elif y > 4000:
				return 'Down'
			elif x > 4000:
				return 'Right'
			elif y < 1000:
				return 'Up'
		except:
			print("exception")
			return ''