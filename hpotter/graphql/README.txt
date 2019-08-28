--- Required files ---
Mongodb needs to be installed and running on localhost:27017 (default) to do this.
https://docs.mongodb.com/manual/administration/install-community/

--- How to run ---

NOTE:mongodb needs to be installed and running
1) navigate to hpotter/graphql/summoning/
2) Start the graphql server with the following command:
	python manage.py runserver
3) navigate to localhost:/8000 to see the graphiql interface

---- How to migrate db changes ---

python manage.py makemigrations
python manage.py migrate

--- Useful links ---
https://www.howtographql.com/graphql-python/1-getting-started/
https://stackoverflow.com/questions/54259453/graphene-resolver-for-nested-custom-object