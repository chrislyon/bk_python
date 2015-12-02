from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Client, Produit, Fourn, Stock, Compteur
import datetime
import random
 
engine = create_engine(BASE_NAME)
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Compteurs 
r = Compteur()
r.nom = "FACTURE"
r.val = 1
session.add(r)

r = Compteur()
r.nom = "COMCLI"
r.val = 1
session.add(r)

r = Compteur()
r.nom = "COMFOU"
r.val = 1
session.add(r)
session.commit()

#Client
n = 10
for c in range(1,n):
	r = Client()
	r.nom = "CLIENT%02d" % c
	print("Creation de %s " % r.nom)
	session.add(r)
	session.commit()
#Produit
n = 10
for c in range(1,n):
	r = Produit()
	r.desig = "PROD%02d" % c
	r.prix = random.randint(50, 2000)
	print("Creation de %s " % r.desig)
	session.add(r)
	session.commit()
#Fourn
n = 10
for c in range(1,n):
	r = Fourn()
	r.nom = "FOU%02d" % c
	print("Creation de %s " % r.nom)
	session.add(r)
	session.commit()
#Stock
prods = session.query(Produit).all()
for p in prods:
	r = Stock()
	r.depot = 'D1'
	r.produit = p
	r.qstock = 0
	print("Creation de %s/%s " % (r.depot,p.desig))
	session.add(r)
	session.commit()
