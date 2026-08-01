# Python - Almost a circle

Introduction to Python Programming and Databases — ALU.

A small class hierarchy exercising inheritance, private attributes with
validated getters and setters, `*args` and `**kwargs`, JSON
serialization and unit testing.

`Base` manages ids and JSON handling, `Rectangle` inherits from it, and
`Square` inherits from `Rectangle` since a square is a rectangle with
equal sides.

## Running the tests

    $ python3 -m unittest discover tests
    $ python3 -m unittest tests/test_models/test_base.py

 Files

| File | Description |
| --- | --- |
| models/base.py | Manages ids, JSON serialization and file storage |
| models/rectangle.py | A rectangle with validated size and position |
| models/square.py | A square, inheriting everything from Rectangle |
| tests/test models/ | Unit tests mirroring the models folder |


