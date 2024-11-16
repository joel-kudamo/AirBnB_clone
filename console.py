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
        return

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
        cmdargs = self.check_cmdarg(args)
        if cmdargs is not None:
            checkKey = f"BaseModel.{cmdargs[1]}"
            print(HBNBCommand.__instances.get(checkKey, "** no instance found **"))
            HBNBCommand.__instances = {}
        else:
            return

    def check_cmdarg(self, args):
        """custom function to check if class, class.id exists or
is missing"""
        cmdargs = args.split()
        if len(cmdargs) > 0:
            if cmdargs[0] == "BaseModel":
                if (len(cmdargs)) > 1:
                    try:
                        with open("file.json", "r", encoding="utf-8") as f:
                          HBNBCommand.__instances  = json.load(f)
                          return cmdargs
                    except (OSError, FileNotFoundError):
                        print("** no instance found **")    
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
        cmdargs = self.check_cmdarg(args)
        if cmdargs is not None:
            del HBNBCommand.__instances[f"BaseModel.{cmdargs[1]}"]
            with open("file.json", "w", encoding="utf-8") as f:
                json.dump(HBNBCommand.__instances, f, indent=2)
            HBNBCommand.__instances = {}
        else:
            return
        
    def do_update(self, args):
        """ Updates an instance based on the class name and id
by adding or updating attribute (save the change into the JSON file)
        """
        pass

    def do_all(self, args):
        """ Prints all string representation of
all instances based or not on the class name"""
        cmdargs = args.split()
        if len(cmdargs) == 0 or cmdargs[0] == "BaseModel":
            try:
                with open("file.json", "r", encoding="utf-8") as f:
                    HBNBCommand.__instances  = json.load(f)
                for keys in HBNBCommand.__instances.keys():
                        print(HBNBCommand.__instances[keys])
            except (OSError, FileNotFoundError):
                pass
        else:
            print("** class doesn't exist **")
        HBNBCommand.__instances = {}


if __name__ == '__main__':
    HBNBCommand().cmdloop()