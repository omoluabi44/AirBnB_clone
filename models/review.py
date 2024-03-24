#!/usr/bin/python3
""" a module that defines Review of Airbnb """


from models.base_model import BaseModel

class Review(BaseModel):
    """ a class that defines Review of Airbnb """

    place_id = ""
    user_id = ""
    text = ""
