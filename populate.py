from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Livre, Compte, Releve, Ecriture
import datetime
 
engine = create_engine(BASE_NAME)
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

## On vire tout
for m in ( Livre, Compte, Releve, Ecriture ):
	session.query(m).delete()

session.commit()

## Creation d'un Livre de comptes
L = Livre()
L.name = "LIVRE 1"
session.add(L)
session.commit()

## Creation de plusieurs comptes
C1 = Compte()
C1.name = "BNP:123456"
C1.livre = L
session.add(C1)
C2 = Compte()
C2.name = "POSTE:654321"
C2.livre = L
session.add(C2)

session.commit()

## Creation d'un releve et de quelques ecritures
R = Releve()
R.name = "Premier releve de test"
R.livre = L

E = Ecriture()
E.compte = C1
E.libelle = "Ecriture no 1"
E.d_ecr = datetime.datetime.now()
E.montant = 1200
E.releve = R
session.add(E)

session.commit()

E = Ecriture()
E.compte = C2
E.libelle = "Ecriture no 2"
E.d_ecr = datetime.datetime.now()
E.montant = 110.12
E.releve = R
session.add(E)

session.commit()
