##
## Classe Livre
##

import sqlite3

script1 = """
			create table Compte ( 
				C_CODE VARCHAR(10), 
				C_DESC VARCHAR(30)
			);
			create table Ecriture( 
				E_CPT VARCHAR(10),
				E_SENS VARCHAR(1), 
				E_DATE DATE, 
				E_LIBEL VARCHAR(30),
				E_MONTANT NUMBER(10.2)
			);
"""


class Livre():
	def __init__(self):
		self.nom = "Livre"
		self.datafile = ":memory:"
		self.cnx = None
		self.opened = False

	def open(self):
		self.cnx = sqlite3.connect(self.datafile)
		self.opened = True

	def initialise(self):
		if self.opened:
			self.cnx.executescript( script1 )

	def do_sql(self, sql):
		if self.cnx:
			cur = self.cnx.cursor()
			cur.execute(sql)
			return True, cur.fetchall()
		else:
			err("Livre non ouvert")
			return False, []

if __name__ == '__main__':
	L = Livre()
	L.nom = "TEST"
	L.open()
	L.initialise()
	s,r = L.do_sql("insert into Compte (C_CODE, C_DESC) values ( 'BQ1', 'BANCAIRE1' ) ")
	s,r = L.do_sql("insert into Compte (C_CODE, C_DESC) values ( 'BQ2', 'BANCAIRE2' ) ")
	s,r = L.do_sql("select rowid, C_CODE, C_DESC from Compte")
	print("Status = %s Resultat %s " % (s,r))
	s,r = L.do_sql("create table TEST ( id integer, nom varchar(20) )")
	print("Status = %s Resultat %s " % (s,r))
	s,r = L.do_sql("insert into TEST (id, nom) values (1, 'TEST01')")
	s,r = L.do_sql("insert into TEST (id, nom) values (2, 'TEST02')")
	s,r = L.do_sql("insert into TEST (id, nom) values (3, 'TEST03')")
	s,r = L.do_sql("insert into TEST (id, nom) values (4, 'TEST04')")
	print("Status = %s Resultat %s " % (s,r))
	s,r = L.do_sql("select rowid, * from TEST")
	print("Status = %s Resultat %s " % (s,r))
