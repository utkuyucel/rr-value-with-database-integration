import datetime
import json
import requests as req
import sqlite3 as sql

class Database:

	def __init__(self):
		# self.main_money = main_money
		self.con = sql.connect("rr.db")
		self.cur = self.con.cursor()
		self.API_SERVER = "https://utkuyucel35.pythonanywhere.com/rr/"
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS Hisseler ( \
			Id INTEGER PRIMARY KEY AUTOINCREMENT, \
			Name TEXT NOT NULL, \
			Optimal REAL NOT NULL, \
			RR REAL NOT NULL, \
			Percentage REAL NOT NULL, \
			Alpha REAL NOT NULL, \
			Time_ DATETIME \
			)"
		)

	def getFromAPI(self, main_money, rr_ratio):
		"""
		Getting the optimal value data from API
		"""
		self.main_money = main_money
		self.rr_ratio = rr_ratio
		self.URL = self.API_SERVER + str(self.main_money) + "/" + str(self.rr_ratio)

		self.output = json.loads(req.get(self.URL).text)

		self.value = self.output["value"]
		self.percentage = self.output["percentage"]
		self.alpha = self.output["alpha"]

		return self.value, self.percentage, self.alpha

	def commitDb(self):
		"""
		Commiting Data to Database
		"""
		self.con.commit()

	def addToDb(self, name, value, rr_ratio, percentage, alpha):
		"""
		Adding Data to Database
		"""
		self.name = name
		self.value = value
		self.rr_ratio = rr_ratio
		self.percentage = percentage		
		self.alpha = alpha

		sqlvar = "INSERT INTO Hisseler(Name, Optimal, RR, Percentage, Alpha, Time_) VALUES(?,?,?,?,?,?)"
		self.cur.execute(sqlvar, ( self.name.upper(), self.value, self.rr_ratio, self.percentage, self.alpha, datetime.datetime.now()))
		self.commitDb()

		print("Added to DB.")

	def showAll(self):
		"""
		Showing data from Database
		"""
		check = "SELECT * FROM Hisseler ORDER BY RR DESC"
		self.cur.execute(check)
		out = self.cur.fetchall()
		print("Id       Name    Optimal         Rr    Percentage       alpha")
		print("----------------------------------------------------------------")
		for i in out:
			print(i[0],"\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4], "\t\t", i[5])

		print("----------------------------------------------------------------")

	def deleteValue(self, id):
		"""
		Deleting a value from Database by its Id
		"""
		self.id = id
		delete = "DELETE FROM Hisseler WHERE Id = " + str(id)
		self.cur.execute(delete)
		self.commitDb()
		print(f"{id} id'li değer silindi.")

	def deleteAll(self):
		"""
		Deleting all rows from the database.
		"""
		delete_all = "DELETE FROM Hisseler"
		self.cur.execute(delete_all)
		self.commitDb()
		print("Veritabanındaki bütün veriler silindi.")

	

        
        