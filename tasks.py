from invoke import task, run

@task
def hello():
	print("Hello World")

@task
def update_git():
	run('rm data.db')
	run('find -name __pycache__ -exec rm {} \;')
	run('git status')
