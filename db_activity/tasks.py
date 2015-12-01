from invoke import task, run

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
	run('rm -f data.db')
	run('python definitions.py')
	run('python populate.py')
