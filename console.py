#!/usr/bin/python3
""" Contains command line interpreter """

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF (self, line):
        """ EOF Program to exit command console """
        return True

    def do_quit(self, line):
        """ Quit program to exit the console """
        return True

    def emptyline(self):
        """ an empty line + enter should do noting """
        return False

""" creaes a BaseModel instance into JSON file 
    creates a new class and prints its id
"""
    def do_create(self, line):
        if 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
