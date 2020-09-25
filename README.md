# Simple CRUD for an court case API

## How to run

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

The server will be running in 127.0.0.1:8000

## API endpoints

- /api/court/
   - Returns the full list of court decisions saved or used to POST a new object

- /api/court/<int:id>
   - Passing the `id` along the API can either do a PUT or DELETE method in a single object

- /api/court/personal/<int:id_cliente>
   - Returns all records to a specific `id_cliente`

- /api/court/decision/<int:id_cliente>
   - Returns the sum of decisions to a specific `id_cliente` in a 3 options dict
