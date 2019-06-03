

.PHONY: run-venv

run-venv:
	rm -rf venv/
	test -f venv/bin/activate || virtualenv -p $(shell which python3) venv
	. venv/bin/activate ; \
	pip install -Ur requirements.txt ;\
	pip freeze | sort > requirements.txt
	touch venv/bin/activate  # update so it's as new as requirements-to-freeze.txt
	
	 

run-migrates:
	python3 manage.py makemigrations ; \
	python3 manage.py migrate ; \
	python3 manage.py createsuperuser --email root@root.com --username root ; \

run-dev:
	python3 manage.py test
	python3 manage.py runserver
