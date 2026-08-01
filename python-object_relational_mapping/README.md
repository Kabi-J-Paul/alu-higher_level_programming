# Python - Object-relational mapping

Introduction to Python Programming and Databases — ALU.

Two ways of reaching a MySQL database from Python: first with raw SQL
through the MySQLdb module, then with SQLAlchemy, where tables are
mapped to Python classes and no SQL is written by hand.

## Files

| File | Description |
| --- | --- |
| 0-select states.py | Lists all states with MySQLdb |
| 1-filter states.py | Lists states whose name starts with N |
| 2-my filter states.py | Filters by name using format, unsafe |
| 3-my safe filter states.py | The same query, safe from SQL injection |
| 4-cities by state.py | Lists cities with their state name |
| 5-filter cities.py | Lists the cities of one state |
| model state.py | Maps the State class to the states table |
| 7-model state fetch all.py | Lists all State objects |
| 8-model state fetch first.py | Prints the first State object |
| 9-model state filter a.py | Lists states containing the letter a |
| 10-model state my get.py | Prints the id of a named state |
| 11-model state insert.py | Adds the state Louisiana |
| 12-model state update id 2.py | Renames the state with id 2 |
| 13-model state deletea.py | Deletes states containing the letter a |
| model city.py | Maps the City class to the cities table |
| 14-mdel city fetchb _state.py | Lists cities with their state |

