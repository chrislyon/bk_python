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
	session = connect()
	r = """
		select numcom, numlig, produit_id, qcom, qliv
		from ligcli
		where qcom-qliv > 0
		order by produit_id
	"""
	ligs = session.execute(r)
	#pdb.set_trace()
	for l in ligs:
		print("Cde %s No %s Prod=%s QCOM=%8d QLIV=%8d" % (l.numcom, l.numlig, l.produit_id, l.qcom, l.qliv ))
	session.close()


def run():
	get_besoins()
 

if __name__ == '__main__':
	run()
