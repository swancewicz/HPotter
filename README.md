
# HPotter
A simple to install and run Honey Pot.

[![Build Status](https://travis-ci.org/drsjb80/HPotter.svg?branch=master)](https://travis-ci.org/drsjb80/HPotter)

## Running and developing

To install the necessary packages, do:

    pip install -r requirements.txt

To run the honeypot itself, do:

    python3 -m hpotter.hpotter

To run the SQL to JSON webserver, do:

    python3 -m hpotter.jsonserver

Once the jsonserver is running, you can see the current data by loading the
ajax.html file that is in the directory above into your web browser.

To see the current contents of the database, do:
To open sqlite cli with database --> your path might be different to database
--> sqlite </path/to/database/main.db>

To see tables available
.tables

To check table setup
.schema <table name>

To turn on header in table when query. Helps identify tables
.header on
.mode column

To see all data in table
SELECT * FROM <table_name>

The JSON API is easy to query. To get all the data, go to localhost:8080:

    curl localhost:8080

If you're interested in a particular table, reference that:

    curl localhost:8080/sh

If you want to use JSONP, pass a callback:

    curl localhost:8080/?callback=jQuery

To get JSON in the form to use with jTables, do:

    curl localhost:8080/?handd=true

## Directory structure
hpotter/

This is the main honeypot executable. It looks in plugins and runs all the
plugins found there.

plugins/

This is where the protocol-specific plugins reside. They are based on
https://docs.python.org/3/library/socketserver.html  The generic.py file is
a good place to start for creating your own plugins.

jsonserver/

Where the SQL to JSON web server resides.    

#### PUT IN HERE HOW TO LAUNCH GEO_LOCTION #######
