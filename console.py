#!/usr/bin/python3
"""The console for the AirBnB project"""
import cmd
import shlex
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The console for the AirBnB project"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to a JSON file and
        prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
