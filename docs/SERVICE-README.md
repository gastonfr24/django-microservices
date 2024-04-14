# Django Auth Microservices

## About this project

## How to configure

### Build the project with Docker

```
docker-componse build
```

### Create Django Project (optional)
```
docker-compose run backend_service django-admin startproject core .
```
### Run the microservice
```
docker-componse up -d
```
### Console
```
docker-compose exec backend_service bash
```