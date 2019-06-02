#SHELL := /bin/bash

# venv1/bin/activate:
# 	weeeee
# 	rm -rf venv1/
# 	test -f venv1/bin/activate || virtualenv -p $(shell which python3) venv1
# 	. venv1/bin/activate ;\
# 	pip install -Ur requirements.txt ;\
# 	pip freeze | sort > requirements.txt
# 	touch venv1/bin/activate  # update so it's as new as requirements-to-freeze.txt

.PHONY: run-venv1

run-venv1:
	rm -rf venv1/
	test -f venv1/bin/activate || virtualenv -p $(shell which python3) venv1
	. venv1/bin/activate ; \
	pip install -Ur requirements.txt ;\
	pip freeze | sort > requirements.txt
	touch venv1/bin/activate  # update so it's as new as requirements-to-freeze.txt
	
	 

run-migrates:
	python3 manage.py makemigrations ; \
	python3 manage.py migrate ; \
	python3 manage.py createsuperuser --email root@root.com --username root ; \

run-dev:
	python3 manage.py test
	python3 manage.py runserver
