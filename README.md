# DRF API Project

A small django app that let's user to import JSON, stores it to models and enables user to list it and view details. The project
was created using django rest framework.

## Prerequisites
- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docker-docs.netlify.app/compose/install/#install-compose)
- [tox](https://pypi.org/project/tox/#description) (optional, for running tests and linters)

## Running the Project
Build the Docker images and run the containers:

`docker-compose up -d --build`

Do not forget to migrate the database:

`docker-compose exec web python manage.py migrate`

After that, you can access the application in [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

To run the tests and linters execute:

`tox`

## API Structure

The project integrates swaggerUI, which enables you to view the structure of the API on:

[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

As you can see there, the POST `import/` endpoint parses JSON and stores the models, that are in correct format into
the database. You can find the import at [http://127.0.0.1:8000/import/](http://127.0.0.1:8000/import/)

The models that will be stored: 

```
{
  "AttributeValue": {
    "id": 1,
    "hodnota": "modrá"
  }
}

{
  "Catalog": {
    "id": 1,
    "nazev": "nazev"
  }
}

{
  "Catalog": {
    "id": 1,
    "nazev": "",
    "products_ids": [1, 2, 3, 5]
  }
}

```

The products_ids attribute of Catalog model is optional, but if present must be list otherwise won't be saved.
Every other model and (Catalog, AttributeValue) in wrong format will be parsed out and not stored.

The app also implements 2 GET endpoints:

`http://127.0.0.1:8000/detail/<str:model_name>/` -> Display all data for models. Possible values are `attribute_value` and `catalog`

`http://127.0.0.1:8000/detail/<str:model_name>/<int:pk>/` -> Display for specific `attribute_value` and `catalog` based on their id.

