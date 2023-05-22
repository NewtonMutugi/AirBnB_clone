#!/usr/bin/python3
"""The console for the AirBnB project"""
import cmd


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
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                from models.base_model import BaseModel
                new = BaseModel()
                new.save()
                print(new.id)
            except ModuleNotFoundError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                from models.base_model import BaseModel
                from models import storage
                args = arg.split()
                if args[0] != "BaseModel":
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print("** instance id missing **")
                else:
                    my_dict = storage.all()
                    key = args[0] + "." + args[1]
                    obj = my_dict[key]
                    # print(key)
                    print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                from models.base_model import BaseModel
                from models import storage
                args = arg.split()
                if args[0] != "BaseModel":
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    del storage.all()[key]
                    storage.save()
            except ModuleNotFoundError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name"""
        from models import storage
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            try:
                from models.base_model import BaseModel
                args = arg.split()
                if args[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    print([str(value) for value in storage.all().values()])
            except ModuleNotFoundError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                from models.base_model import BaseModel
                from models import storage
                args = arg.split()
                if args[0] != "BaseModel":
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print("** instance id missing **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    key = args[0] + "." + args[1]
                    setattr(storage.all()[key], args[2], args[3])
                    storage.save()
            except ModuleNotFoundError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
