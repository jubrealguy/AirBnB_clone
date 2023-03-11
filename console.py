#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand for interpreting """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ To exit the program """
        return True

    def do_EOF(self, arg):
        """ To exit the program """
        return True

    def do_emptyline(self):
        """ When no argument provided """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
