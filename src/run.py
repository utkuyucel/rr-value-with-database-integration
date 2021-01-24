import datetime
from dbase import Database

app = Database()
main_money = 4000 

while True:
	print("1-Deger ekle\n2-Hisseler tablosundaki verileri göster\n3-Veri sil\n4-Tüm verileri sil\n5-Optimal degerleri topla \
										\n0-Çıkış\n")
	check = input("->")

	if (check == "1"):
		try:
			name = input("Hissenin ismini giriniz: ")
			rr_ratio = float(input("Risk/Ödül oranını giriniz: "))

			value, percentage, alpha = app.getFromAPI(main_money, rr_ratio)
			app.addToDb(name, value, rr_ratio, percentage, alpha)

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

	elif (check == "4"):
		check = input("Bütün veriler silinecek, onay veriyor musunuz ? (e/h): ")

		if (check.upper() == "E"):
			app.deleteAll()

		elif (check.upper() == "H"):
			print("İşlem iptal edildi.\n")
			continue

		else:
			print("Böyle bir seçenek bulunmamaktadır.\n")
			continue

	elif (check == "5"):
		x = app.sumOptimal()
		kalan = int(main_money - x)
		print(f"Toplam optimal para degeri: {x} TL")
		print(f"Kalan para: {kalan} TL\n")


	elif (check == "0"):
		print("Çıkış yapılıyor.")
		break

	else:
		print("Böyle bir seçenek bulunmamaktadır.")

		
