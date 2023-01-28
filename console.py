#!/usr/bin/python3
""" Contains command line interpreter """

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """Creates hbnb as a  prompt"""

    __classes = {"BaseModel"}

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
