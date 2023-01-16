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

As you can see there, the `import/` endpoint parses JSON and stores the models in correct format into
the database. You can find the import at [http://127.0.0.1:8000/import/](http://127.0.0.1:8000/import/)

The models that will be stored: 

```
       {
	      "AttributeValue": {
		    "id": 1,
		    "hodnota": "modrá"
	      }
	    }
```
```
    {
      "Catalog": {
        "id": 1,
      }
    }
```
or 
```
    {
      "Catalog": {
        "id": 1,
        "products_ids": [
          1,
          2,
          3,
          5
        ]
      }
    }
```

The app also implements 4 GET endpoints:

[http://127.0.0.1:8000/detail/attribute_value/](http://127.0.0.1:8000/detail/attribute_value/) -> Display all data for AttributeValue

[http://127.0.0.1:8000/detail/attribute_value/<int:pk>/](http://127.0.0.1:8000/detail/attribute_value/<int:pk>/) -> Display data for AttributeValue with specific id 

[http://127.0.0.1:8000/detail/catalog/](http://127.0.0.1:8000/detail/catalog/) -> Display all data for Catalog

[http://127.0.0.1:8000/detail/catalog/<int:pk>/](http://127.0.0.1:8000/detail/catalog/<int:pk>/) -> Display data for Catalog with specific id 