import datetime
from dbase import Database

app = Database()
main_money = 3500

while True:
	print("1-Deger ekle\n2-Hisseler tablosundaki verileri göster\n3-Veri sil\n0-Çıkış\n")
	check = input("->")

	if (check == "1"):
		try:
			name = input("Hissenin ismini giriniz: ")
			rr_ratio = float(input("Risk/Ödül oranını giriniz: "))

			value, percentage = app.getFromAPI(main_money, rr_ratio)
			app.addToDb(name, value, rr_ratio, percentage)

		except:
			print("\n\nHata.\n\n")

	elif (check == "2"):
		app.showAll()

	elif (check == "3"):
		id = int(input("Silmek istediğiniz verinin id'sini giriniz: "))

		try:
			app.deleteValue(id)
			print("\nDeğer başarıyla silindi.\n")

		except:
			print("Veritabanında bu id'de bir değer bulunmamaktadır.")

	elif (check == "0"):
		print("Çıkış yapılıyor.")
		break

	else:
		print("Böyle bir seçenek bulunmamaktadır.")

		