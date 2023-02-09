""" console interpreter """
import cmd
from models import storage
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """Creates hbnb as a  prompt"""

    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Place": Place,
                 "Amenity": Amenity,
                 "Review": Review
                 }

    def do_EOF(self, line):
        """ EOF Program to exit command console """
        return True

    def do_quit(self, line):
        """ Quit program to exit the console """
        return True

    def emptyline(self):
        """ an empty line + enter should do nothing """
        return False

    def do_create(self, new_class):
        """ Creates a new instance of Basemodel
        saves it(to the JSON file) and prints the id"""
        if not new_class:
            print("** class name missing **")
        else:
            if new_class not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                new_class = eval(new_class + "()")
                new_class.save()
                print(new_class.__dict__['id'])

    def do_show(self, *argv):
        """ Prints the string representation of an instance based on
        the class name and id """
        items = argv[0].split(" ")
        if (len(items)) == 1 and items[0] == '':
            print("** class name missing **")
        else:
            if items[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                if (len(items)) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        class_found = storage.all()[items[0] + "." + items[1]]
                        print(class_found)
                    except KeyError:
                        print("** no instance found **")

    def do_destroy(self, *argv):
        """Deletes an instance based on the class name and id
        (saves the changes into the json file) """

        items = argv[0].split(" ")
        if (len(items)) == 1 and items[0] == '':
            print("** class name missing **")
        else:
            if items[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                if (len(items)) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[items[0] + "." + items[1]]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")

    def do_all(self, class_type):
        """ prints all string representation of all instances based
        or not on the class name """
        all_objects = storage.all()
        temp_dict = []

        if not class_type:
            for key, value in all_objects.items():
                temp_dict.append(str(value))
            print(temp_dict)
        else:
            if class_type not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for key, value in enumerate(all_objects):
                    out = all_objects[value]
                    if class_type == out.__class__.__name__:
                        temp_dict.append(str(out))
                print(temp_dict)

    def do_update(self, *argv):
        """ updates an instance based on the class\
         name and id by adding or updating
        attribute ( save the change into the json file)"""
        items = argv[0].split(" ")

        if (len(items)) == 1 and items[0] == '':
            print("** class name missing **")
        else:
            if items[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                if (len(items)) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        temp_dict = storage.all()[items[0] + "." + items[1]]
                        if (len(items)) < 3:
                            print("** attribute name missing **")
                        else:
                            if (len(items)) == 3:
                                print("** value missing **")
                            elif (len(items)) == 4:
                                # get the attribute specified and update it
                                if type(items[3]) in [str, float, int]:
                                    # set attr build in function
                                    txt = items[3]
                                    temp_dict.__dict__[items[2]] = txt[1:-1]
                                    temp_dict.save()

                    except KeyError:
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
