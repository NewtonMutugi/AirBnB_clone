#!/usr/bin/python3
"""The console for the AirBnB project"""
import cmd
from datetime import datetime
from models import storage
from models.engine.file_storage import attributes
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


my_classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review",
}


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
                args = arg.split()
                if args[0] not in my_classes:
                    print("** class doesn't exits **")
                    return
                instance = eval(args[0])()
                storage.save()
                print(instance.id)
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
                if args[0] not in my_classes:
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print("** instance id missing **")
                else:
                    my_dict = storage.all()
                    key = args[0] + "." + args[1]
                    if key not in my_dict:
                        print("** no instance found **")
                        return
                    obj = my_dict[key]
                    # print(key)
                    print(obj)
            except ModuleNotFoundError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                from models import storage
                args = arg.split()
                # Test whether arg[0] is in my_classes dictionary
                if args[0] not in my_classes:
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
                if args[0] not in my_classes:
                    print("** class doesn't exist **")
                else:
                    # print([str(value) for value in storage.all().values()])
                    objl = []
                    for obj in storage.all().values():
                        if len(args) > 0 and args[0] == obj.__class__.__name__:
                            objl.append(obj.__str__())
                        elif len(args) == 0:
                            objl.append(obj.__str__())
                    print(objl)
            except ModuleNotFoundError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                from models import storage
                args = arg.split()
                my_dict = storage.all()
                if args[0] not in my_classes:
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print("** instance id missing **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                elif "{}.{}".format(args[0], args[1]) not in my_dict.keys():
                    print("** no instance found **")
                else:
                    key = args[0] + "." + args[1]
                    obj = my_dict[key]
                    attribute_name = args[2]
                    attribute_value = args[3]

                    # Check the class type and update the attribute accordingly
                    class_attributes = attributes(self, args[0])
                    if attribute_name in class_attributes:
                        attribute_type = class_attributes[attribute_name]
                        attribute_value = attribute_type(attribute_value)
                        setattr(obj, attribute_name, attribute_value)
                        obj.save()
                    else:
                        print("** attribute doesn't exist **")
            except ModuleNotFoundError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
