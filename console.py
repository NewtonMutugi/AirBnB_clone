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

dot_commands = ['all', 'count', 'show', 'destroy', 'update']

types = {
    'number_rooms': int, 'number_bathrooms': int,
    'max_guest': int, 'price_by_night': int,
    'latitude': float, 'longitude': float
}


class HBNBCommand(cmd.Cmd):
    """The console for the AirBnB project"""
    prompt = '(hbnb) '

    def precmd(self, line):
        """Pre command to check for dot commands"""

        _cmd = _cls = _id = _args = ''  # initialize line elements

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in dot_commands:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')

                # if arguments exist beyond _id
                pline = pline[2].strip()
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')

            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help command for quit"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        """Help command for EOF"""
        print("EOF command to exit the program\n")

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
                    print("** class doesn't exist **")
                    return
                instance = eval(args[0])()
                storage.save()
                print(instance.id)
            except ModuleNotFoundError:
                # print("** class doesn't exist **")
                return

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
                    return
                elif len(args) == 1:
                    print("** instance id missing **")
                    return
                else:
                    key = args[0] + "." + args[1]

                    if key not in storage.all():
                        print("** no instance found **")
                        return
                    else:
                        del storage.all()[key]
                        storage.save()

            except KeyError:
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
                    return
                elif len(args) == 1:
                    print("** instance id missing **")
                    return
                elif len(args) == 2:
                    print("** attribute name missing **")
                    return
                elif len(args) == 3:
                    print("** value missing **")
                    return
                elif "{}.{}".format(args[0], args[1]) not in my_dict.keys():
                    print("** no instance found **")
                    return
                else:
                    key = args[0] + "." + args[1]
                    attribute_name = args[2]
                    attribute_value = args[3]

                    # first determine if kwargs or args
                    if '{' in args[2] and '}' in args[2] and type(
                            eval(args[2])) is dict:
                        kwargs = eval(args[2])
                        args = []
                        for k, v in kwargs.items():
                            args.append(k)
                            args.append(v)
                    else:
                        args = args[2]
                        if args and args[0] == '\"':
                            second_quote = args.find('\"', 1)
                            attribute_name = args[1:second_quote]
                            args = args[second_quote + 1:]

                        args = args.partition(' ')

                        if not attribute_name and args[0] != ' ':
                            attribute_name = args[0]
                        if args[2] and args[2][0] == '\"':
                            attribute_value = args[2][1:args[2].find('\"', 1)]

                        # if att_val was not quoted arg
                        if not attribute_value and args[2]:
                            attribute_value = args[2].partition(' ')[0]

                        args = [attribute_name, attribute_value]

                    # retrieve dictionary of current objects
                    new_dict = storage.all()[key]

                    # iterate through attr names and values
                    for i, att_name in enumerate(args):
                        if (i % 2 == 0):
                            att_val = args[i + 1]
                            if not att_name:
                                print("** attribute name missing **")
                                return
                            if not att_val:
                                print("** value missing **")
                                return
                            if att_name in types:
                                att_val = types[att_name](att_val)

                            # update dictionary with name, value pair
                            new_dict.__dict__.update({att_name: att_val})

                    new_dict.save()
            except KeyError:
                print("** class doesn't exist **")

    def help_update(self):
        """ """
        print("Usage: update <class_name> <id> <attribute_name> \
<attribute_value>")

    def help_create(self):
        """ """
        print("Usage: create <class_name>")

    def help_show(self):
        """ """
        print("Usage: show <class_name> <id>")

    def help_destroy(self):
        """ """
        print("Usage: destroy <class_name> <id>")

    def help_all(self):
        """ """
        print("Usage: all <class_name>")

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                args = arg.split()
                class_name = args[0]
                if class_name not in my_classes:
                    print("** class doesn't exist **")
                    return
                else:
                    count = 0
                    objects = storage.all()
                    for obj in objects.values():
                        if class_name == obj.__class__.__name__:
                            count += 1
                    print(count)
            except ModuleNotFoundError:
                print("** class doesn't exist **")

    def help_count(self):
        """ """
        print("Usage: count <class_name>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
