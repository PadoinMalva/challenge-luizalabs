# challenge-luizalabs
Challenge Luiza Labs

## Run - Dev

```bash
# Create and started venv of project
$ make run-venv
```

```bash
# Run first time and create django user admin
$ make run-dev
```

## Test Api
```bash
curl -H 'Accept: application/json; indent=4' -u root:root http://127.0.0.1:8000/users/
```

