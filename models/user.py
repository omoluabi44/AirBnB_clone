#!/usr/bin/python3
""" a module that defines User of Airbnb """


from models.base_model import BaseModel

class User(BaseModel):
    """ a class that defines user of Airbnb """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
