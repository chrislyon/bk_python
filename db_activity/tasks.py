##
## A Lancer avec invoke
##
from invoke import task, run
import random

@task
def hello():
	print("Hello World")

@task
def purge():
	run('rm -f data.db')
	run("find . -name '__pycache__' -exec rm -fr {} \;")
	#run('git status')

@task
def test():
	print(" Creation de la base ")
	run('./purge_DEV.sh')
	run('python definitions.py')
	print(" Populons la base ")
	run('python populate.py')

@task(test)
def client():
	for x in range(1,random.randint(1,5)):
		print(" Client %s " % x )
		run('python client.py')
