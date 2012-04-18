from main import *
class Punkt():
	
	def __def__(self, x, y, maxX, maxY)
		self.wspolrzedne = (x,y) #tupla, lub krotka czyli nic nie moze ulec zmianie 
		self.wymiaryBoiska = (maxX, maxY)
		self.dozwoloneRuchy = []
		self.wypelnijDozwolonePunkty()
		self.odwiedzony = False
	
	def dajPunkt(self, x,y):
		#ma znalezc na liscie slef.punkty ounkt ktory ma wspolrzedne x i y
		# Wiemy, ze na liscie NIGDY nie ma 2 punktow o takich samych wspolrzednych
		for punkt in punkty:
			if punkt.wspolrzedne == (x,y):
				return punkt
		return False
	
	def wypelnijDozwoloneRuchy(self):
		# Co mamy do dyspozycji:
		# Liste ruchow - zmienna globalna (tablica) = sciezkaRuchow
		# Liste wszystkich punktow na planszy - zmienna globalna = punkty
		# Wymiary boiska - zmienna klasowa (krotka dokladnie) = self.wymiaryBoiska
		# Wspolrzedne punktu ktoremu chcemy generowac ruchy - zmienna klasowa (krotka) = self.wspolrzedne
		# Kazdy punkt ma w sobie informacje czy byl juz w grze odwiedzony - zmienna klasowa kazdego punktu = self.odwiedzony
		# Mamy tez sciezkeRuchow ktora jest zmienna gloabalna - sciezkaRuchow
		#
		# Rozwazania przypadkow:
		# 1. Niedozwolone ruchy:
		#    - przejscie z punktu A do punktu B gdzie w sciezce istnial ruch z B do A a takze jesli istnial ruch
		#	z a do b
		#   
		#    - nie wolno chodzic po bramce
		#
		# 2. Dozwolone ruchy
		#    - te ujete  w adnotacji JEDEN
		
		# 3. Potrzebujemy sprawdzic tylko 8 punktow (te na lewo..prawo itd)
		mozliwePunkty = []
		biezacyX = self.x
		biezacyY = self.y
		if self.dajPunkt(biezacyX, biezacyY+1) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX, biezacyY+1))
		if self.dajPunkt(biezacyX, biezacyY-1) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX, biezacyY-1))
		if self.dajPunkt(biezacyX-1, biezacyY) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX-1, biezacyY))
		if self.dajPunkt(biezacyX+1, biezacyY) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX+1, biezacyY))
		if self.dajPunkt(biezacyX-1, biezacyY+1) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX-1, biezacyY+1))			
		if self.dajPunkt(biezacyX+1, biezacyY+1) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX+1, biezacyY+1))
		if self.dajPunkt(biezacyX-1, biezacyY-1) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX-1, biezacyY-1))
		if self.dajPunkt(biezacyX+1, biezacyY-1) != False:
			mozliwePunkty.append(self.dajPunkt(biezacyX+1, biezacyY-1))
		
		for punkt in mozliwePunkty:
			 	
			
""" 
adnotacja jeden
do jakich punktow mozna dojsc z punktu 5,5:
punkt wyzej: 5,6
punkt nizej: 5,4
punkt na lewo 4,5
punkt na prawo 6,5
punkt lewo gora 4,6
punkt prawo gora 6,6
punkt lewo dol 4,4
punkt prawo dol 6,4 

"""
	
	
