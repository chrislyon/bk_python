## -------------------------
## Librairie des sequences
## -------------------------

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Compteur


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

def run():
	## Creation d'un compteur TEST
	cpt = 'TEST'
	cr_Compteur(cpt)
	## Valeur Courante
	## next_val
	## Valeur Courante
 

if __name__ == '__main__':
	run()
