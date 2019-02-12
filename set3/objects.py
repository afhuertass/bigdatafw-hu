
import numpy as np 

class Carat():

	def __init__( self , x ):

		self.data = {}

		self.data["energyRate"] = float(x[0])
		self.data["batteryHealth"]  = str( x[1])
		self.data["batteryTemp"] = float( x[2] )
		self.data["batteryVoltage"] = float( x[3] )
		self.data["cpuUsage"] = float( x[4] )
		self.data["distanceTraveled"] = str( x[5] )
		self.data["mobilData"] = str( x[6])
		self.data["mobileSt"] = str( x[7] )
		self.data["mobileNet"] = str( x[8])
		self.data["netType"] = str( x[9] )
		self.data["roaming"] = str( x[10] )
		self.data["screenBright"] = float( x[11])
		self.data["wifiSpeed"] = str( x[12] )
		self.data["wifiStre"] = int( x[13] )
