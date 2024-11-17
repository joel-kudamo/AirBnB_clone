#!/usr/bin/python3
"""(module) This module contains the HBNBCommand object"""
import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """This object inherits from the cmd class
    to create a custom command interpreter for
    managing AirBnB clone database"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Prevents termination of program by blankline
        + ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
(to the JSON file) and prints the id
        """
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args == "BaseModel":
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an
instance based on the class name and id
        """
        try:
            if self.check_cmdarg(args):
                print(self.check_cmdarg(args))
            HBNBCommand.__instances = {}
        except KeyError as e:
            print(e)

    def check_cmdarg(self, args):
        """custom function to check if class, class.id exists or
is missing"""
        cmdargs = args.split()
        if len(cmdargs) > 0:
            if cmdargs[0] == "BaseModel":
                if (len(cmdargs)) > 1:
                    try:
                        with open("file.json", "r", encoding="utf-8") as f:
                            HBNBCommand.__instances = json.load(f)
                            checkKey = f"BaseModel.{cmdargs[1]}"
                            if HBNBCommand.__instances.get(checkKey)\
                                    is not None:
                                return HBNBCommand.__instances.get(checkKey)
                            else:
                                raise KeyError("** no instance found **")
                    except (OSError, FileNotFoundError):
                        raise KeyError("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and
id (save the change into the JSON file).
        """
        try:
            if self.check_cmdarg(args):
                cmdargs = args.split()
                del HBNBCommand.__instances[f"BaseModel.{cmdargs[1]}"]
                with open("file.json", "w", encoding="utf-8") as f:
                    json.dump(HBNBCommand.__instances, f, indent=2)
            HBNBCommand.__instances = {}
        except KeyError as e:
            print(e)

    def do_update(self, args):
        """ Updates an instance based on the class name and id
by adding or updating attribute (save the change into the JSON file)
        """
        try:
            if self.check_cmdarg(args):
                cmdargs = args.split()
                key = f"{cmdargs[0]}.{cmdargs[1]}"
                if len(cmdargs) > 2:
                    if len(cmdargs) == 4:
                        HBNBCommand.__instances[key][cmdargs[2]] = cmdargs[3]
                        with open("file.json", "w", encoding="utf-8") as f:
                            json.dump(HBNBCommand.__instances, f, indent=2)
                        HBNBCommand.__instances = {}
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
        except KeyError as e:
            print(e)

    def do_all(self, args):
        """ Prints all string representation of
all instances based or not on the class name"""
        cmdargs = args.split()
        if len(cmdargs) == 0 or cmdargs[0] == "BaseModel":
            self.openfile()
        else:
            print("** class doesn't exist **")
        HBNBCommand.__instances = {}

    def openfile(self):
        """Opens file.json and saves the stringified dictionary
to the class private attribute
        """
        try:
            with open("file.json", "r", encoding="utf-8") as f:
                HBNBCommand.__instances = json.load(f)
            for keys in HBNBCommand.__instances.keys():
                print(HBNBCommand.__instances[keys])
        except (OSError, FileNotFoundError):
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
