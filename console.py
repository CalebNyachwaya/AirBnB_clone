#!/usr/bin/python3
"""Console to begin my application"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """Console class begins"""

    prompt = '(hbnb) '
    def do_quit(self, arg):
        "Quit command to exit the program"

        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """Pass or do nothing via emptyline"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
