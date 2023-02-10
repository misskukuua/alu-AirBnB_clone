#!/usr/bin/python3
"""store by serialization and deserialization"""

import json



class FileStorage:
    """ A class that serializes instances to Json file
        and deserializes Json file back to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dict _objects"""
        return self.__objects

  
    def new(self, obj):
        """
            sets in  __objects the obj with key(<obj class name>.id)
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects to a Json file"""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """deserializes the Json file  back to objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(self.__file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    self.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass
