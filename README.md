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




## Test Api Exemples
ADD employee (POST)
```bash
curl -d '{"name":"Daniel Padoin", "email":"teste@teste.com", "department":"Teste" }' -H "Content-Type: application/json" -X POST http://localhost:8000/employee/addemployee
```

List employee (GET)
```bash
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/listemployees
```



