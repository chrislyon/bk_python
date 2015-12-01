## -------------------------------------
## DECLARATIONS DE LA BASE DE DONNEES
## -------------------------------------

import os
import sys
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
 
Base = declarative_base()

BASE_NAME = 'sqlite:///data.db'

class BASE_TABLE():
	id = Column(Integer, primary_key=True)
	d_cre = Column(DateTime, default = datetime.datetime.now() )
	d_mod = Column(DateTime, default = datetime.datetime.now(), onupdate=datetime.datetime.now() )

## Classe Livre 
class Livre(Base, BASE_TABLE):
	__tablename__ = 'LIVRES'
	name = Column(String(30), nullable=False, unique=True)

class Compte(Base, BASE_TABLE):
	__tablename__ = 'COMPTES'
	name = Column(String(30), nullable=False, unique=True)
	livre_id = Column(Integer, ForeignKey('LIVRES.id'))
	livre = relationship(Livre)

class Releve(Base, BASE_TABLE):
	__tablename__ = 'RELEVES'
	name = Column(String(50), nullable=False)
	livre_id = Column(Integer, ForeignKey('LIVRES.id'))
	livre = relationship(Livre)


class Ecriture(Base, BASE_TABLE):
	__tablename__ = 'ECRITURES'
	compte_id = Column(Integer, ForeignKey('COMPTES.id'))
	compte = relationship(Compte)
	releve_id = Column(Integer, ForeignKey('RELEVES.id'))
	releve = relationship(Releve)
	libelle = Column(String(30))
	d_ecr = Column(Date)
	montant = Column(Numeric(12,2))

## -----------------------------
## Classe de TEST et d'exemple
## -----------------------------
 
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine(BASE_NAME)
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
