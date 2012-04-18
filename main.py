from punkt import Punkt

global sciezkaRuchow
global czyJuzKoniec
global ostatecznyZwyciezca
global punkty

punkty = []
ostatecznyZwyciezca = 0
czyJuzKoniec = False
sciezkaRuchow = []


class Plansza():

	#DONE	
	# Klasa Plansza w swoim konstruktorze przyjmuje 2 zmienne oznaczajace wymiary planszy
	def __init__(self, x, y):
		
		self.maxX = x
		self.maxY = y
		self.inicjalizujPunkty()
		
	#DONE	
	def inicjalizujPunkty(self):
		for x in range(self.maxX):
			for y in range(self.maxY):
				p = Punkt(x,y,self.maxX, self.maxY)
				punkty.append(p)
		self.biezacyPunkt = self.dajPunkt(self.maxX/2, self.maxY/2)
		sciezkaRuchow.append(self.biezacyPunkt)
		self.biezacyGracz = 1
		
		# Ustawiamy wszystkie "skrajne" punkty na odwiedzone, zeby symulowalo to brzegi boiska 
		for x in range(self.maxX):
			p = self.dajPunkt(x,0)
			p.odwiedzony = True
			p = dajPunkt(x,self.MaxY)
			p.odwiedzony = True
		
		for y in range(self.maxY):
			p = self.dajPunkt(0, y)
			p.odwiedzony = True;
			p = dajPunkt(self.MaxX,y)
			p.odwiedzony = True
		p = self.dajPunkt(self.maxX/2, 0)
		p.odwiedzony = False
		
		p = self.dajPunkt(self.maxX/2, self.maxY)
		p.odwiedzony = False
		
		# Musimy odznaczyc wejscia do bramki (bramka ma zawsze zszerokosc 2), oraz dorobic 3 punkty za bramkami.
		punktZaBramkaDolna1 = Punkt(self.maxX/2 - 1,-1, self.maxX, self.maxY )
		punktZaBramkaDolna2 = Punkt(self.maxX/2,-1, self.maxX, self.maxY )
		punktZaBramkaDolna3 = Punkt(self.maxX/2 + 1,-1, self.maxX, self.maxY )
		
		punktZaBramkaDolna1.odwiedzony = True;
		punktZaBramkaDolna2.odwiedzony = True;
		punktZaBramkaDolna3.odwiedzony = True;
		punkty.append(punktZaBramkaDolna1)
		punkty.append(punktZaBramkaDolna2)
		punkty.append(punktZaBramkaDolna3)
		
		punktZaBramkaGorna1 = Punkt(self.maxX/2 - 1,self.maxY+1, self.maxX, self.maxY )
		punktZaBramkaGorna2 = Punkt(self.maxX/2,self.maxY+1, self.maxX, self.maxY )
		punktZaBramkaGorna3 = Punkt(self.maxX/2 + 1,self.maxY+1, self.maxX, self.maxY )
		
		punktZaBramkaGorna1.odwiedzony = True  #zeby sie pilka odbijala od sciany
		punktZaBramkaGorna2.odwiedzony = True
		punktZaBramkaGorna3.odwiedzony = True
		punkty.append(punktZaBramkaGorna1)
		punkty.append(punktZaBramkaGorna2)
		punkty.append(punktZaBramkaGorna3)
		#generowanie poczatkowej sciezki ktora symuluje obramowanie boiska
		sciezkaRuchow.append(punktZaBramkaGorna1)
		sciezkaRuchow.append(punktZaBramkaGorna2)
		sciezkaRuchow.append(punktZaBramkaGorna3)
		
		for x in range(self.maxX/2 + 1, self.maxX):
			sciezkaRuchow.append(self.dajPunkt(x, self.maxY))
		
		igreki = []
		for y in range(self.maxY):
			igreki.append(y)
		for y in igreki.reverse():
			sciezkaRuchow.append(self.dajPunkt(self.maxX, y))
			
		iksy = []
		for x in range(self.maxX-1, self.maxX/2+1):
			iksy.append(x)
		for x in iksy.reverse():
			sciezkaRuchow.append(self.dajPunkt(x, 0))
			
		sciezkaRuchow.append(punktZaBramkaDolna3)
		sciezkaRuchow.append(punktZaBramkaDolna2)
		sciezkaRuchow.append(punktZaBramkaDolna1)	
		
		iksy = []
		for x in range(self.maxX/2-1):
			iksy.append(x)
		for x in iksy.reverse():
			sciezkaRuchow.append(self.dajPunkt(x,0))
		
		for y in range(1, slef.maxY):
			sciezkaRuchow.append(self.dajPunkt(0, y))
		
		for x in range(1, self.maxX/2-1):
			sciezkaRuchow.append(self.dajPunkt(x, self.maxY);	
			
		sciezkaRuchow.append(self.dajPunkt(punktZaBramkaGorna1))		
		
			
	def wykonajRuch(self, punkt):
	
		#na poczatku bedziemy musieli sprawdzic czy ruch jest w ogole dozwolony
		if not self.czyRuchDozwolony(punkt):
			return False
		self.biezacyPunkt = punkt
		sciezkaRuchow.append(self.biezacyPunkt)	
		self.biezacyPunkt.wypelnijDozwolonePunkty()
		
		#sprawdzanie czy czasem gracz sie nie zablokowal
		if len(self.biezacyPunkt.dozwoloneRuchy) == 0:
			if self.biezacyGracz == 1:
				self.zakonczGreUstawZwyciezce(2)
			else:
				self.zakonczGreUstawZwyciezce(1)
		if(self.biezacyPunkt.odwiedzony  == True):
			if self.czyTenPunktToBramka(self.biezacyPunkt):
				self.zakonczGreUstawZwyciezce(self.biezacyGracz)
				return True
		self.biezacyPunkt.odwiedzony = True
		self.zmienGracza()
		return True 	
		
			
	def czyRuchDozwolony(self, punkt):
		if (punkt in self.biezacyPunkt.dozwoloneRuchy):
			return True
		else:
			return False
			
	# [DONE]			
	def dajPunkt(self, x,y):
		#ma znalezc na liscie slef.punkty ounkt ktory ma wspolrzedne x i y
		# Wiemy, ze na liscie NIGDY nie ma 2 punktow o takich samych wspolrzednych
		for punkt in punkty:
			if punkt.wspolrzedne == (x,y):
				return punkt
		return False		
				
	#DONE				
	def zmienGracza(self):
		if(self.biezacyGracz == 1):
			slef.biezacyGracz = 2
		else: 
			self.biezacyGracz = 1
			
	#DONE						
	def czyTenPunktToBramka(self, punkt):
		bramwkoweWspolrzedne = [(self.maxX/2-1,-1), (self.maxX/2,-1), ( self.maxX/2+1,-1), (self.maxX/2-1, self.maxY+1), (self.maxX/2, self.maxY+1), (self.maxX/2+1, self.maxY+1)]	
		if punkt.wspolrzedne in bramkoweWspolrzedne:
			return True
		else
			return False
				
	def zakonczGreUstawZwyciezce(self, gracz):
		ostatecznyZwyciezca = gracz
		czyJuzKoniec = True
		
			
			
			
			
			
			
