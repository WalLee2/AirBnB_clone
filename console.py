#!/usr/bin/python3
"""
Entry point to the command interpreter.
"""
import cmd


class Console(cmd.Cmd):
    """
    Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    Avoid execution of the user just presses enter as well.
    """
    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def do_help(self, line):

    if __name__ == "__main__":
        prompt = Console()
        prompt.prompt = "(hbnb) "
        Console().cmdloop()
