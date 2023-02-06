#!/usr/bin/python3
""" Contains command line interpreter """

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
from shlex import split


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

    def do_create(self, line):
        """ creates a BaseModel instance into JSON file-creates a
         new class and prints its id
        """
        if not line:
            print("** class name missing **")
        else:
            if line not in self.__classes:
                print("** class doesn't exist **")
            else:
                line = eval(line + "()")
                line.save()
                print(line.__dict__['id'])

    def do_show(self, line):
        """Prints the string representation of an instance
          based on the class name and id
       """
        show = line.split()
        objdict = models.storage.all()

        if len(show) == 0:
            """print class name is name is missing If 
            the class name is missing,
            """
            print("** class name missing **")
            return

        elif len(show) == 1:
            """If the id is missing, print ** instance id missing **"""
            print("** instance id missing **")
            return

        elif show[0] not in HBNBCommand.__classes:
            """If the class name doesn’t exist,
             print ** class doesn't exist **
            """
            print("** class doesn't exist **")
            return

        elif "{}.{}".format(show[0], show[1]) not in objdict:
            print("** no instance found **")
            return
        else:
            print(objdict["{}.{}".format(show[0], show[1])])

    def do_destroy(self, line):
        """
       Deletes an instance based on the class name and id
       Save changes into a JSON file
       """
        destroy = line.split()
        des_objdict = models.storage.all()
        if len(destroy) == 0:
            print("** class name missing **")
            return

        elif len(destroy) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(destroy[0], destroy[1])
            if key not in des_objdict.keys():
                print("** no instance found **")
            else:
                del des_objdict[key]
                models.storage.save()

    def do_all(self, line):
        """
       Prints all string representation of all instances
       based or not on the class name.
       """
        dall = line.split()
        if len(dall) > 0 and dall[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        else:
            obj1 = models.storage.all()
            objects = obj1.values()
            obj2 = []
            for obj in objects:
                if len(dall) > 0 and dall[0] == obj.__class__.__name__:
                    obj2.append(obj.__str__())
                elif len(dall) == 0:
                    obj2.append(obj.__str__())
            print(obj2)

    def do_update(self, line):
        """
       updates an instance based on the class name and id
       by adding or updating attribute
       save the change into the JSON file

       Usage: update <class name> <id>
       <attribute name> "<attribute value>"
       """
        update = line.split()
        objdict = storage.all()

        if len(update) == 0:
            print("** class name missing **")
            return False
        if update[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(update) == 1:
            print("** instance id missing **")
            return False
        key = "{}.{}".format(update[0], update[1])
        if key not in objdict.keys():
            print("** no instance found **")
            return False
        if len(update) == 2:
            print("** attribute name missing **")
            return False
        if len(update) == 3:
            print("** value missing **")
            return False
        else:
            cast = type(eval(update[3]))
            arg_3 = update[3]
            arg_3 = arg_3.strip("'")
            arg_3 = arg_3.strip('"')
            setattr(objdict.get(key), update[2], cast(arg_3))
            objdict[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
