#!/usr/bin/python3
"""
store by serialization and deserialization 
"""
import os.path
import json


class FileStorage:
    """ A class that serializes instances to Json file
    and deserializes Json file back to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dict _objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in objects the obj with key 
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to a Json file"""
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f)

    def reload(self):
        """deserializes the Json file  back to objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        lst = {'BaseModel': BaseModel, 'User': User,
               'Place': Place, 'City': City, 'Amenity': Amenity,
               'State': State, 'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(lst[value['__class__']](**value))
