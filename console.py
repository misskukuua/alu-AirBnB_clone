#!/usr/bin/python3
"""Defines AirBnb console."""
import cmd
import re
import models
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __all_classes = {"BaseModel": BaseModel,
                     "User": User,
                     "State": State,
                     "City": City,
                     "Place": Place,
                     "Amenity": Amenity,
                     "Review": Review
                     }

    def emptyline(self):
        """
        Called when an empty line is entered.
        If this method is not overridden like this,
        """
        pass

    def default(self, arg):
        """This is the default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command -> exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal -> exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Crates a new instance, saves it (to JSON file) and prints the `id`.
                Usage: create <class>
                """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__all_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            models.storage.save()

    def do_show(self, args):
        """Usage: to show <class> <id> or <class>.show(<id>)
        Display string representation of a class instance of given id.
        """
        arg_list = args.split()
        objdict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return

        object_key = "{}.{}".format(arg_list[0], arg_list[1])

        if object_key not in objdict:
            print("** no instance found **")
            return
        else:
            print(objdict[object_key])

    def do_destroy(self, args):
        """Usage: to destroy <class> <id> or <class>.destroy(<id>)
        Delete class instance of given id."""

        arg_list = args.split()
        all_objects = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]

        object_key = "{}.{}".format(class_name, instance_id)

        if object_key not in all_objects.keys():
            print("** no instance found **")
        else:
            del all_objects[object_key]
            storage.save()

    def do_all(self, args):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of given class
        If no class is specified, display all instantiated objects."""

        arg_list = args.split()
        all_objects = storage.all()
        object_list = []
        if len(arg_list) == 0:
            for obj in all_objects.values():
                object_list.append(obj.__str__())
            print(list(object_list))
            return

        if len(arg_list) > 0 and arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        class_name = arg_list[0]
        object_list = []

        for obj in all_objects:
            if class_name == all_objects[obj].__class__.__name__:
                object_list.append(str(all_objects[obj]))
        print(object_list)

    def do_count(self, args):
        """Usage: to count <class> or <class>.count()
        Retrieve number of instances of given class."""

        arg_list = args.split()
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__all_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + '.' + tokens[1]) not in obj_dict:
                print("** no instance found **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                obj = obj_dict[tokens[0] + '.' + tokens[1]]
                if tokens[2] in obj.__class__.__dict__.keys():
                    v_type = type(obj.__class__.__dict__[tokens[2]])
                    obj.__dict__[tokens[2]] = (v_type(tokens[3]))
                else:
                    obj.__dict__[tokens[2]] = tokens[3]
                models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
