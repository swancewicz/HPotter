

--- How to create python virtual environment ---

--- How to run ---

1) navigate to hpotter/graphql
2) Start the venv with:
	1) python -m venv venv
	2) one of the two:
	(mac) source venv/bin/activate
	(windows, in git bash) source venv/Scripts/activate
3) cd folder to summoning (cd summoning)
4) Start the graphql server with the following command:
	python manage.py runserver
5) navigate to localhost:/8000


---- How to migrate db changes ---

python manage.py makemigrations
python manage.py migrate

--- Useful links ---
https://www.howtographql.com/graphql-python/1-getting-started/