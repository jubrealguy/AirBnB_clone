#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand for interpreting
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """
        To exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        To exit the program
        """
        return True

    def emptyline(self):
        """
        When no argument provided
        """
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg in classes.keys():
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
	elif arg[0] not in self.classes.keys():
                print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] +'.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
       args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.classes.keys():
                print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] +'.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):




if __name__ == "__main__":
    HBNBCommand().cmdloop()
