# Callback
==================

### Overview

A simple API driven web application to track the calls that need to be 
transferred.  It sends out an email when a new request is made, adds it to a
list to be monitored.  You can go view each one, where you can see all notes
regarding the callback.  You can update the callback, which also sends out an
email, same when updating the status.

### Installation

> git clone https://github.com/3cko/callbacks.git

Once in the repo:

> python virtualenv.py flask
> flask/bin/pip -r Requirements.txt
> python db_create.py

Once you have your servers IP, run the application from within:

> flask/bin/python run.py runserver -h xxx.xxx.xxx.xxx -p 8182

### Usage

#### Web
Load up the URL in your favorite browser.

#### API

The API only accepts and returns JSON

|HTTP Method|URI|Action|
|:-|:-|:-|
|GET|http://[hostname]/api/v1.0/callbacks|Retrieve list of callbacks|
|GET|http://[hostname]/api/v1.0/callbacks/[callback]|Retrieve a callback|
|POST|http://[hostname]/api/v1.0/callbacks|Create new callback|
|PUT|http://[hostname]/api/v1.0/callbacks/[callback]|Update a callback|

POST request accepts all fields
-ddi:
-name:
-phone:
-ticket:
-platform:
-details:
-status:

PUT requests accept 2 fields
-details
-status

Return a full list of call backs
http://xxx.xxx.xxx.xxx/api/v1.0/callbacks

Return specific callback by case number
http://xxx.xxx.xxx.xxx/api/v1.0/callbacks/#

### To-Do

-Better error handling for web interface and the API
-User Login
-Admin Panel
-Consistant updates to the callback list
-~~Email threading~~
-Consider migrating the database to mongodb
-Pageination
-Commenting Code
-Refractor**

