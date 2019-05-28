venv/bin/activate: 
	rm -rf venv/
	test -f venv/bin/activate || virtualenv -p $(shell which python3) venv
	. venv/bin/activate ;\
	pip install -Ur requirements.txt ;\
	pip freeze | sort > requirements.txt
	touch venv/bin/activate  # update so it's as new as requirements-to-freeze.txt

.PHONY: run-venv

run-venv:
	venv/bin/activate
	. venv/bin/activate ;

run-dev:
	python3 manage.py createsuperuser --email root@root.com --username root ; \
	python3 manage.py makemigrations employees ; \
	python3 manage.py migrate employees ; \