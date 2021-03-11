# Django + Docker = DjanDo

DjanDo is a light-weight command-line interface for interacting with Django in a Docker development environment.

# Installation

```shell
$ pip install djando
```

# Usage

In a Django root folder project run:

```shell
$ djando init
```

This command will add the following files to your project:

```
youproject/
    | ...
    | runtimes/
    | docker-compose.yml
    | ...
```

After that, start the container:

```shell
$ djando up
```

> Note: when running `djando up` first time DjanDo will try to create a `venv` folder and install dependencies
> from `requirements.txt`

# Environment Variables

DjanDo will load all environment variables (needed for docker-compose.yml) from a `.env` file at the root project folder.

# Proxyed Commands

DjanDo proxy commands to `docker-compose`. For example:

```shell
$ djando manage runserver
```
Will be proxyed to

```shell
$ docker-compose exec -u djando django.test python manage.py runserver
```

List of all proxyed commands:

| Command  | Proxyed Command | Example |
| ---- | :-------: | :-------: |
| python | python | djando python --version |
| pip | pip | djando pip install -r requirements.txt |
| django-admin | django-admin| djando django-admin check |
| manage | python manage.py | djando manage runserver |
| psql | PGPASSWORD=${PGPASSWORD} psql -U ${POSTGRES_USER} ${POSTGRES_DB} | djando psql |
| shell or bash | bash | djando bash |
| root-shell | bash (root user)| djando root-shell |

Any other command will be passed to `docker-compose` directly, for example:

```shell
$ djando up # will be proxyed to docker-compose up 
$ djando up -d # will be proxyed to docker-compose up -d
$ djando down # will be proxyed to docker-compose down
$ djando ps # will be proxyed to docker-compose ps 
```

