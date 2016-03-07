##
## LIVRAISON CLIENT
##


# Pour toutes les lignes de commandes a livrer 
#  (Par client / Par Produit  ... )
#  - Allouer en fonction de la date de commande
#  - et si QTOCK - QCOM > 0
#  - decrementer le stock

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

## Retourne les lignes de commandes a livrer
def get_bl_aliv():
	session = connect()
	r = """
		select numcom, numlig, produit_id, qcom, qliv
		from LIGCLI
		where qcom-qliv > 0
		order by numcom, numlig
	"""
	b = session.execute(r)
	bls = [ (x[0], x[1], x[2]) for x in b ]
	session.close()
	return bls

def get_stock(depot, pro):
	session = connect()
	s = select([Stock]).where(Stock.produit_id==pro).where(Stock.depot==depot)
	r = session.execute(s)
	f = r.fetchone()
	session.close()
	return f.qstock


def run():
	DEPOT = 'D1'
	## Pour toute les lignes de commandes a livrer
	b = get_bl_aliv()
	for l in b:
		print(" Je traite : ", l)
		## On recupere le stock
		s = get_stock(DEPOT, l[2])
		print("Stock Pro Depot %s : %s = %s " % (DEPOT, l[2], s))

 

if __name__ == '__main__':
	run()
