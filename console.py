import cmd

class HBNBCommand(cmd.Cmd):
    """This object inherits from the cmd class
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit
    
    def do_EOF(self):
        """EOF command to exit the program
        """

    def emptyline(self):
        return 

if __name__ == '__main__':
    HBNBCommand().cmdloop()