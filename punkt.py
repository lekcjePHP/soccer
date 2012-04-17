from main import *
class Punkt():
	
	def __def__(self, x, y, maxX, maxY)
		self.wspolrzedne = (x,y) #tupla, lub krotka czyli nic nie moze ulec zmianie 
		self.wymiaryBoiska = (maxX, maxY)
		self.dozwoloneRuchy = []
		self.wypelnijDozwolonePunkty()
		self.odwiedzony = False
		
	def wypelnijDozwoloneRuchy(self):
		# Co mamy do dyspozycji:
		# Liste ruchow - zmienna globalna = sciezkaRuchow
		# Liste wszystkich punktow na planszy - zmienna globalna = punkty
		# Wymiary boiska - zmienna klasowa (krotka dokladnie) = self.wymiaryBoiska
		# Wspolrzedne punktu ktoremu chcemy generowac ruchy - zmienna klasowa (krotka) = self.wspolrzedne
		# Kazdy punkt ma w sobie informacje czy byl juz w grze odwiedzony - zmienna klasowa kazdego punktu = self.odwiedzony
		
		# Rozwazania przypadkow:
		# 1. Niedozwolone ruchy:
		#    - chodzic po "scianie"
		#    - przejscie z punktu A do punktu B gdzie w sciezce istnial ruch z B do A
		#    - Wyjsc poza plansze
		#    - nie wolno chodzic po bramce
		#
		# 2. Dozwolone ruchy
		#    - te ujete  w adnotacji JEDEN
		pass

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
	
	
