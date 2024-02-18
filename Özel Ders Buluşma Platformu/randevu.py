# <!-- 6. *Randevu Yönetim Sayfası:* - - 
# Öğrencinin veya eğitmenin aldığı/verdiği derslerin görüntülendiği bölüm veya 
# takvim 
# Randevu iptali veya onaylama seçenekleri  -->


from datetime import date


class ders():
	def __init__(self,adı,adresi,bölümler,öğretmen):
		self.__adı= adı
		self.__adresi= adresi
		self.__bölümler= bölümler
		self.öğretmen= öğretmen
		self.__rezervasyonlar= []

	def getAdı(self):
		return self.__adı

	def setAdı(self,yeni_ad):
		self.__adı= yeni_ad
		print("Ders adı değiştirildi")

	def getAdresi(self):
		return self.__adresi

	def setAdresi(self,yeni_adres):
		self.__adresi= yeni_adres
		print("Ders adresi değiştirildi")

	def getBölümler(self):
		print("=========Bölümlerimiz=========")
		for bölüm in self.__bölümler:
			print("""

				Bölüm: {bölüm}

				""".format(bölüm=bölüm))
			print("="*50)

	def bölümEkle(self,yeni_bölüm):
		self.__bölümler.append(yeni_bölüm)
		print("Yeni bölüm eklendi.")

	def getÖğretmenler(self):
		print("=========Öğretmenlerimiz=========")
		for öğretmen in self.__öğretmenler:
			print("""

				İsim: {isim}
				Soyad: {soyad}
				Telefon: {telefon}
				Bölüm: {bölüm}

				""".format(isim=öğretmen.getİsim(),soyad=öğretmen.getSoyad(),telefon=öğretmen.getTelefon(),bölüm=öğretmen.getBölüm()))
			print("="*50)

	def öğretmenEkle(self,yeni_öğretmen):
		self.__öğretmenler.append(yeni_öğretmen)
		print("Yeni öğretmen eklendi.")

	def rezervasyonYap(self,öğrenci,istenenöğretmen,istenentarih):
		müsaitlik= True
		for rezervasyon in self.__rezervasyonlar:
			listedeki_öğrenci= rezervasyon[0]
			listedeki_öğretmen= rezervasyon[1]
			listedeki_tarih= rezervasyon[2]

			if listedeki_öğretmen == istenenöğretmen and listedeki_tarih == istenentarih:
				print("Öğretmenimiz o tarihte müsait değildir.")
				müsaitlik= False
		if müsaitlik:
			self.__rezervasyonlar.append((öğrenci,istenenöğretmen,istenentarih))
			print("Rezervasyon kaydı gerçekleşti.")


	def getRezervasyonlar(self):
		print("="*50)
		print("========Rezervasyonlar========")
		rez_sayısı= 0

		for rezervasyon in self.__rezervasyonlar:
			listedeki_öğrenci= rezervasyon[0]
			listedeki_öğretmen= rezervasyon[1]
			listedeki_tarih= rezervasyon[2]

			print("{öğrenciismi} {öğrencisoyadı} isimli Öğrencinin {rez_tarihi} tarihinde Öğretmen {öğretmenismi} {öğretmensoyadı} ile randevusu vardır.".format(öğrenciismi=listedeki_öğrenci.getİsim(),öğrencisoyadı=listedeki_öğrenci.getSoyad(),rez_tarihi=listedeki_tarih,öğretmenismi=listedeki_öğretmen.getİsim(),öğretmensoyadı=listedeki_öğretmen.getSoyad()))
			print("="*50)
			rez_sayısı+=1
		if rez_sayısı == 0:
			print("Hiçbir rezervasyon yok.")



class Birey():
	def __init__(self,isim,soyad,telefon):
		self.__isim= isim
		self.__soyad= soyad
		self.__telefon= telefon

	def getİsim(self):
		return self.__isim

	def getSoyad(self):
		return self.__soyad

	def getTelefon(self):
		return self.__telefon



class öğretmen(Birey):

	öğretmen_sayısı= 0


	def __init__(self,isim,soyad,telefon,bölüm):
		super().__init__(isim,soyad,telefon)
		öğretmen.öğretmen_sayısı_artır()
		self.__bölüm= bölüm

	def getBölüm(self):
		return self.__bölüm

	@classmethod
	def öğretmen_sayısı_artır(cls):
		cls.öğretmen_sayısı += 1

class öğrenci(Birey):
	pass



d1= öğretmen("Ali","Tosun","5425454","matematik")
d2= öğretmen("Serhat","Kabak","545455","ingilizce")
d3= öğretmen("Şenay","Sucu","54554554","fizik")

h1= öğrenci("Pınar","Mersinli","554555")
h2= öğrenci("Halil","Kuru","5454545")

bölümler= ["matematik","ingilizce","fizik","kimya"]

ders= ders("Özel Ders","Merkez",bölümler,[d1,d2])

print("="*50)
print("{} hoş geldiniz.".format(ders.getAdı()))


ders.getRezervasyonlar()

ders.rezervasyonYap(h1,d2,date.today())
ders.rezervasyonYap(h2,d2,date.today())


ders.getRezervasyonlar()

print("Toplam Öğretmen sayısı: ",öğretmen.öğretmen_sayısı)



