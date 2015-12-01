select 
	livres.name,releves.name, comptes.name, LIBELLE, montant, d_ecr 
from 
	ECRITURES, COMPTES, RELEVES, LIVRES 
where 
	    compte_id=comptes.id 
	and releve_id=releves.id 
	and releves.livre_id=livres.id;
