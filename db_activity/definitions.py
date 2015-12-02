## -------------------------------------
## DECLARATIONS DE LA BASE DE DONNEES
## -------------------------------------

import os
import sys
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime, Date, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
 
Base = declarative_base()

BASE_NAME = 'sqlite:///data.db'

class BASE_TABLE():
	" Classe commune a toute les autres"
	id = Column(Integer, primary_key=True)
	d_cre = Column(DateTime, default = datetime.datetime.now() )
	d_mod = Column(DateTime, default = datetime.datetime.now(), onupdate=datetime.datetime.now() )

class Client(Base, BASE_TABLE):
	"Le fichier client"
	__tablename__ = 'CLIENTS'
	nom = Column(String(20), nullable=False, unique=True)

class Produit(Base, BASE_TABLE):
	"Les produits"
	__tablename__ = 'PRODUITS'
	desig = Column(String(30), nullable=False, unique=True)
	#prix = Column(Numeric(12,2))
	prix = Column(BigInteger)

class Fourn(Base, BASE_TABLE):
	"Les fournisseurs"
	__tablename__ = 'FOURN'
	nom = Column(String(20), nullable=False, unique=True)
	delai = Column(Integer)

class Stock(Base, BASE_TABLE):
	"Le stock par depot"
	__tablename__ = 'STOCK'
	depot = Column(String(10), nullable=False)
	produit_id = Column(Integer, ForeignKey('PRODUITS.id'))
	produit = relationship(Produit)
	qstock = Column(Integer)

class ComCli(Base, BASE_TABLE):
	"Les commandes clients"
	__tablename__ = 'COMCLI'
	numcom = Column(Integer, unique=True)
	datcom = Column(DateTime, default = datetime.datetime.now() )
	client_id = Column(Integer, ForeignKey('CLIENTS.id'))
	client = relationship(Client)
	facture = Column(Integer)

class LigCli(Base, BASE_TABLE):
	"Les lignes de commandes clients"
	__tablename__ = 'LIGCLI'
	numcom = Column(Integer)
	numlig = Column(Integer)
	produit_id = Column(Integer, ForeignKey('PRODUITS.id'))
	produit = relationship(Produit)
	qcom = Column(Integer)
	#prix = Column(Numeric(12,2))
	prix = Column(BigInteger)
	qliv = Column(Integer)
	qfac = Column(Integer)

class LigFou(Base, BASE_TABLE):
	"Les commandes fournissuers"
	__tablename__ = 'LIGFOU'
	numcom = Column(Integer, unique=True)
	numlig = Column(Integer)
	fou_id = Column(Integer, ForeignKey('FOURN.id'))
	fou = relationship(Fourn)
	produit_id = Column(Integer, ForeignKey('PRODUITS.id'))
	produit = relationship(Produit)
	qcom = Column(Integer)
	#prix = Column(Numeric(12,2))
	prix = Column(BigInteger)
	dprevu = Column(DateTime)
	qrecu = Column(Integer)
	
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine(BASE_NAME)
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
