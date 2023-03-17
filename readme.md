# This is a base layout Repository for creating a Flask app.

### First create a Virual environement after cloning the repo.

To do this:
```
python3 -m venv venv
```

### Now activate the virtual environment using the following command:

In linux: 
```
source venv/bin/activate
```

On windows:
```
 ./venv/Script/activate
```

### After that install all the requirements required.

To do this:
```
Pip install -r requirements.txt
```

### Now that the dependencies are installed. Creata a database named data.db using the create_db.py file. This creates a SQLite database.

To do this:
```
python3 create_db.py
```

### Now you can run the program with serve.py

```
python3 serve.py
```