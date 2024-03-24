# AIRBNB CLONE
![hBnB](https://github.com/omoluabi44/AirBnB_clone/assets/110730304/b6fde21a-1119-49b1-bb46-5dd77bb2a22c)

# Project Name

## Overview

This project aims to create a command-line interpreter (CLI) in Python using the cmd module. The CLI allows users to manage objects within the project, such as creating, retrieving, updating, and destroying objects. The commands can be executed both interactively and non-interactively.

## Learning Objectives

- Creating a Python package
- Implementing a command interpreter in Python using the cmd module
- Understanding and implementing unit testing in a large project
- Serializing and deserializing a Class
- Writing and reading JSON files
- Managing datetime
- Understanding UUIDs
- Using *args and **kwargs
- Handling named arguments in a function

## Execution

### Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
### Non Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
```
## USAGE
Follow below step to get started

Clone repo to your local machine
```https://github.com/omoluabi44/AirBnB_clone.git```

Change directory
``` cd Airbnb_clone ```

run the console
``` ./console.py ```

### EXECUTING COMMANDS
to create user for Airbnb and reurn unique id, run this
```create <classname> ```
in built classes as follows:
   - BaseModel
   - User
   - Amenity
   - Place
   - City
   - State
   - Review
``` create User ```

to view instances created from each classes using specied id run this
``` show <classname> <id> ```
``` show User 47f7e540-3806-42a8-bdbd-c6feba35af63

to show all instance or instances of class, run the code respectivley
```all ```
```all <classname>```