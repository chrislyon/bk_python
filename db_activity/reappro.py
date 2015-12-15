## --------------------
## REAPPRO
## --------------------

# Etape 1 : recup de la liste des besoins
# Etape 2 : pour chaque produit selectionner 1 fourn
# Etape 3 : generer les commandes

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Client, Produit, Fourn, Stock, ComCli, LigCli, LigFou

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

def get_besoins():
	"""
	Calcul des besoins en commande
	"""
	session = connect()
	## Pour verif
	r = """
		select numcom, numlig, produit_id, qcom, qliv
		from ligcli
		where qcom-qliv > 0
		order by produit_id
	"""
	## En vrai
	r = """
		select produit_id, sum(qcom) 'qte'
		from ligcli
		where qcom-qliv > 0
		group by produit_id
		order by produit_id
	"""
	ligs = session.execute(r)
	#pdb.set_trace()
	#for l in ligs:
	#	print("Prod=%s QCOM=%8d " % (l.produit_id, l.qte))
	besoin = [ x for x in ligs ]
	session.close()
	return besoin

def get_fourn():
	session = connect()
	s = select([Fourn.id])
	fous = session.execute(s)
	l = [ x[0] for x in fous]
	session.close()
	return random.choice(l)

def get_delai(fou):
	session = connect()
	s = select([Fourn]).where(Fourn.id==fou)
	r = session.execute(s)
	f = r.fetchone()
	session.close()
	return f.delai

def gnr_comfou(besoin):
	session = connect()
	#pdb.set_trace()
	for b in besoin:
		f = get_fourn()
		delai = get_delai(f)
		C = LigFou()
		C.numcom = seq.Next_val('COMFOU')
		C.numlig = 1
		C.produit_id = b[0]
		C.fou_id = f
		C.qcom = b[1]
		C.prix = 0
		C.qrecu = 0
		C.dprevu = datetime.datetime.now()
		C.dprevu += datetime.timedelta(days=delai)
		print(" Cde %s fou=%s pro=%s qte=%s " % ( C.numcom, C.fou_id, C.produit_id, C.qcom ))
		session.add(C)

	session.commit()
	session.close()


def run():
	## Calcul des besoins
	 b = get_besoins()
	 gnr_comfou(b)
 

if __name__ == '__main__':
	run()
