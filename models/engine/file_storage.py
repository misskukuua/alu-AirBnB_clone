#!/usr/bin/python3
"""store by serialization and deserialization"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """ A class that serializes instances to Json file
        and deserializes Json file back to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dict _objects"""
        return self.__objects

    # def new(self, obj):
    #     """
    #     sets in objects the obj with key
    #     """
    #     key = obj.__class__.__name__ + '.' + obj.id
    #     self.__objects[key] = obj
    def new(self, obj):
        """
            sets in  __objects the obj with key(<obj class name>.id)
        """
        key = obj.__class__.__name__, + ".", obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes objects to a Json file"""
        with open(self.__file_path, mode='w') as file:
            obj_dict = {}
            for key, val in self.__objects.items():
                obj_dict.update[key] = val.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the Json file  back to objects"""
        try:
            with open(self.__file_path, mode='r') as file:
                obj_dict = json.load(file)
                for key in obj_dict.keys():
                    obj_dict2 = obj_dict[key]
                    self.__objects[key] = eval(
                        obj_dict2['__class__'])(**obj_dict2)
        except FileNotFoundError:
            pass
