#!/usr/bin/python3
""" Contains command line interpreter """

import cmd

import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """Creates hbnb as a  prompt"""

    __classes = {"BaseModel": BaseModel}

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
        """ creates a BaseModel instance into JSON file-creates a new class and prints its id """
        if len(line) == 0:
            print('** class name missing **')
            return
        argv = line.split()
        if argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new = eval(argv[0]())
        new = new.save
        print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance
           based on the class name and id
        """
        argv = line.split()
        objdict = models.storage.all()

        if len(argv) == 0:
            """print class name is name is missing If the class name is missing,"""
            print("** class name missing **")
            return

        elif len(argv) == 1:
            """If the id is missing, print ** instance id missing **"""
            print("** instance id missing **")
            return

        elif argv[0] not in HBNBCommand.__classes:
            """If the class name doesn’t exist, print ** class doesn't exist **"""
            print("** class doesn't exist **")
            return

        if "{}.{}".format(argv[0], argv[1]) not in objdict:
            print("** no instance found **")
            return
        else:
            print(objdict["{}.{}".format(argv[0], argv[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
