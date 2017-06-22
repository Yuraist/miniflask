# miniflask
**Miniflask** is a minimal Flask application, which contains recommended file and directory structure for a Flask project. You can use it for starting Flask applications as a foundation. 

### Getting started 
To start with *Miniflask* you should open the miniflask directory and dowload the *Flask* and other requirements (if you didn't). 

```
# In the terminal open miniflask/ and run this: 
$ pip freeze requirements.txt
```

### How to run a server
To run a server with *Miniflask* you should export the app with Flask and run it.

```
# In the terminal run: 

$ export FLASK_APP=app.py
$ flask run

# Your server will be started 
```

### run.py
This is the application's entry point. You run this file to start the Flask server and launch your application.

### config.py
This file contains the configuration variables for your app.

### app/__init__.py
This file initializes the Python module. 

### app/views.py
You need the **views.py** file to manage all the routes for your application. This file will tell Flask what template to display on which path. 

### app/models.py
You need the **models.py** file for representation the database tables in code. Now the file is empty, cause there is no database.

### app/static
You should store your static files (like css, js or img files) here.

### app/templates
You should store your html templates here.