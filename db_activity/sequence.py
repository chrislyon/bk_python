## -------------------------
## Librairie des sequences
## -------------------------
## -------------------------------------
## Pas super efficace mais portable
## -------------------------------------

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Compteur

import pdb


## Connexion
def connect():
	engine = create_engine(BASE_NAME, echo=False)
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def cr_Compteur(nom):
	session = connect()
	c = Compteur()
	c.nom = nom
	c.val = 1
	session.add(c)
	session.commit()
	session.close()

def Curr_val(nom):
	session = connect()
	s = select([Compteur]).where(Compteur.nom==nom)
	r = session.execute(s)
	cpt = r.fetchone()
	session.close()
	return cpt.val

def Next_val(nom):
	session = connect()
	cpt = session.query(Compteur).filter_by(nom=nom).first()
	cpt.val += 1
	r = cpt.val
	session.add(cpt)
	session.commit()
	session.close()
	return r


def run():
	## Creation d'un compteur TEST
	cpt = 'TEST'
	try:
		cr_Compteur(cpt)
	except:
		pass
	## Valeur Courante
	print( "Valeur courante : %s = %s" % (cpt, Curr_val(cpt)))
	## next_val
	print( "Valeur Suivante : %s = %s" % (cpt, Next_val(cpt)))
	## Valeur Courante
	print( "Valeur courante : %s = %s" % (cpt, Curr_val(cpt)))
 

if __name__ == '__main__':
	run()
