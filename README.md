# Kong API Gateway with CDN Integration Python

## Installing Prerequisites

Python `module request`
```shell
$ pip install requests
```
Docker Desktop Windows with `wsl 2`
```shell
$ wsl --update
```

## Getting started

#### Important note
From official github of Kong there is one issue https://github.com/Kong/kong/issues/5324, so we can't use kong's latest docker image. So we will use `kong:1.3.0-alpine` docker image.

Change directory to `src`
```shell
$ cd src
```
Create `kong network`
```shell
$ ./script/create_kong_network
```

Start `postgres`
```shell
$ ./script/start_postgres
```

Migrate `kong database`
```shell
$ ./script/migration_bootstrap
$ ./script/migration_up
```

Migrate `kong admin database`
```shell
$ ./script/prepare_konga
```

Start `kong api gateway`
```shell
$ ./script/start_kong
```

Start `kong admin`
```shell
$ ./script/start_konga
```

Open `kong admin UI` http://localhost:1337/

#### Prepare Microservices CDN Integration
There are one `microservices` example for this demo with 2 script python, `upload.py` and `retrieve.py`. It is just simple `microservice` written in `Python`. Here how to run it

Add `Services` to Kong API Gateway

```shell
$ curl -i -X POST   --url http://localhost:8001/services/   
--data 'name=ecommerce-romi'   
--data 'url=http://apache2.romijulianto.my.id/'
```

Add `Routes` to Kong API Gateway

```shell
$ curl -i -X POST   --url http://localhost:8001/services/ecommerce-romi/routes   
--data 'paths[]=/cdn-assets'
```

Change Directory to `services`

```shell
$ cd services
```
Run `upload.py`

```shell
$ python upload.py
```

Run `retrieve.py`
```shell
$ python retrieve.py
```