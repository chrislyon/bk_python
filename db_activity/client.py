## --------------------
## Prise de commande
## --------------------

#Etape 1 : init + connexion
#Etape 2 : Recup du catalogue
#Etape 3 : Choix du client 
#Etape 4 : Generation de commande

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Client, Produit, Stock, ComCli, LigCli

import sequence as seq

import datetime
import random
import pdb

## Connexion
def connect():
	engine = create_engine(BASE_NAME, echo=False)
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def get_catalog():
	session = connect()
	s = select([Produit.id])
	prods = session.execute(s)
	p = [ x[0] for x in prods]
	session.close()
	return p

def get_client():
	session = connect()
	s = select([Client.id])
	clis = session.execute(s)
	l = [ x[0] for x in clis]
	session.close()
	return random.choice(l)

def get_tarif(prod_id):
	session = connect()
	s = select([Produit]).where(Produit.id==prod_id)
	r = session.execute(s)
	p = r.fetchone()
	session.close()
	return p.prix

def get_prods(cat):
	max_cmd = len(cat)
	nb_pro_cmd = random.randint(0, max_cmd-1)+1
	pros = random.sample(cat, nb_pro_cmd)
	return pros

def gnr_comcli(cli, prods):
	print("Client : %s " % cli )
	print("Nb Produits a commandes : %s " % len(prods) )
	print("Produits commandes : %s " % sorted(prods) )
	print("Generation commande")
	session = connect()
	numcom = seq.Next_val('COMCLI')
	C = ComCli()
	C.numcom = numcom
	C.datcom = datetime.datetime.now()
	C.client_id = cli
	C.facture = 0
	session.add(C)
	print( "Commande No : " , C.numcom )
	n = 1
	for p in prods:
		L = LigCli()
		L.numcom = numcom
		L.numlig = n
		L.produit_id = p
		L.qte = random.randint(1, 5000)
		L.prix = get_tarif(p)
		print("%s : %s" % (n,L))
		n += 1
		session.add(L)
	session.commit()
	session.close()

def run():
	#Get catalog
	catalog = get_catalog()
	#print(catalog)
	#choix du client
	client = get_client()
	#print(client)
	# Choix du catalog
	prods_cmd = get_prods(catalog)
	#Gnr_cmdcli
	gnr_comcli(client, prods_cmd)
 

if __name__ == '__main__':
	run()
