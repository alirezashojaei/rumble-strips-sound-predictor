import winsound
from time import sleep


# The car object to specify properties
class Car:
	def __init__(self, speed, whealbase=2.5):
		self.speed = speed
		self.whealbase = whealbase
		
	def __repr__(self):
		return f"A car with {self.speed}km/h speed and {self.whealbase} meter whealbase"


# Rumble Strip object
class Strip:
	def __init__(self, lenght, gap, number):
		self.gap = gap
		self.lenght = lenght
		self.number = number
	
	def _single_sound(self, car):
		frequency = 120
		dur = int(self.lenght/(car.speed/3600))
		winsound.Beep(frequency, dur)
		return '[#######]'
		
	def sound(self, car):
		for round in range(1, self.number):
			self._single_sound(car)
			dur = self.gap/(car.speed/3.6)
			print(dur)
			sleep(dur)
		else:
			self._single_sound(car)
		
	def passing(self, car):
		self.sound(car)
		
		
# Pieces of asphalt (used as a gap)
class Asphalt:
	
	def __init__(self, lenght):
		self.lenght = lenght
		
	def __repr__(self):
		return f"A {self.lenght}-meter piece of asphalt"
		
	def passing(self, car):
		dur = self.lenght/(car.speed/3.6)
		sleep(dur)


# Specify the car and pass that over the strips

c = Car(10)

asphalt_1 = Asphalt(3)
asphalt_1 = Asphalt(1)
strip_1 = Strip(0.20,0.001,7)
strip_2 = Strip(0.20,0.001,7)

strip_1.passing(c)
strip_1.passing(c)
# asphalt_1.passing(c)
# strip_2.passing(c)
