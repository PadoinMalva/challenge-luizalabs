# challenge-luizalabs
Challenge Luiza Labs

## Run - Dev

```bash
# Create venv of project
$ make run-venv
```

```bash
# Started venv of project
$ . venv/bin/activate
```

```bash
# Run first time to do the migrations and create a superuser on Django
$ make run-migrates
```

```bash
# Run tests and start the API
$ make run-dev
```
## API Endpoints
URL: http://localhost:8000

/admin
- To access Django admin


/employee/addemployee
- Add employee


/employee/listemployees
- List all employees


/employee/removeemployee
- Remove a specific employee



## Test Api Exemples
```bash
# ADD employee (POST)
curl -d '{"name":"Daniel Padoin", "email":"teste@teste.com", "department":"Teste" }' -H "Content-Type: application/json" -X POST http://localhost:8000/employee/addemployee
```

```bash
# List employee (GET)
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/listemployees
```

```bash
# Remove employee (GET)
curl -X DELETE 'http://localhost:8000/employee/removeemployee?email=teste@teste.com'
```




