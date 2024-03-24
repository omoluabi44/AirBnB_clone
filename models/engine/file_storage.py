#!/usr/bin/python3


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ class for my file storage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return all
        """
        return self.__objects

    def new(self, obj):
        """
        return new dict
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save to file
        """
        serialize_object = {}

        for key, value in self.__objects.items():
            if isinstance(value, (Review, Place, Amenity, BaseModel, City, User, State)):
                serialize_object[key] = value.to_dict()
            else:
                serialize_object[key] = value

        with open(self.__file_path, "w") as f:
            json.dump(serialize_object, f)

    def reload(self):
        """
        reload back to json
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                self.__objects[key] = eval(key.split('.')[0])(**value)
        except FileNotFoundError:
            pass

    def get_intances_by_class(self, class_name):
        """
        return instances of all class
        """
        instances = []
        numbers_of_instanecs = 0
        for key, obj in self.__objects.items():
            if key.split(".")[0] == class_name:
                instances.append(obj)
                numbers_of_instanecs += 1
        return instances, numbers_of_instanecs
