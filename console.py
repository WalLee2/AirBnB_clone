#!/usr/bin/python3
"""
Entry point to the command interpreter.
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    Avoid execution of the user just presses enter as well.
    """
    #################
    # Do Commands ###
    #################

    intro = "Welcome to hbnb! Type help for more options."
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return False

    def do_create(self, user_input):
        """Creates a new instance and returns the unique id"""
        if not user_input:
            print("** class name missing **")
        elif user_input in class_check:
            _input = user_input.split()
            new_obj = class_check[_input[0]]()
            new_obj.save()
            storage.reload()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, usr_in):
        """Prints the whole dictionary with the new instance"""
        _input = usr_in.split()
        switch = 0
        switch1 = 0
        objects = storage.all()
        if _input[0] not in class_check:
            print("** class doesn't exist **")
        elif len(_input) < 2:
            num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for letter in _input[0]:
                if letter in num_list:
                    switch1 = 1
            if switch1 == 1:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        elif len(_input) == 2:
            for key in objects.keys():
                if key == _input[1]:
                    print(objects[key])
                    switch = 1
            if switch == 0:
                print("** no instance found **")

    def do_destroy(self, usr_in):
        """Destroys the instance with a specific id"""
        _input = usr_in.split()
        switch = 0
        switch1 = 0
        objects = storage.all()
        if _input[0] not in class_check:
            print("** class doesn't exist **")
        elif len(_input) < 2:
            num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for letter in _input[0]:
                if letter in num_list:
                    switch1 = 1
            if switch1 == 1:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        elif len(_input) == 2:
            for key in objects.keys():
                if key == _input[1]:
                    del objects[key]
                    switch = 1
                    break
            storage.save()
            if switch == 0:
                print("** no instance found **")

    def do_all(self, usr_in):
        _input = usr_in.split()
        objects = storage.all()
        for key in objects.keys():
            if _input:
                if _input[0] not in class_check:
                    print("** class doesn't exist **")
                    break
                if _input[0] == objects[key].__dict__['__class__']:
                    print(objects[key])
            else:
                print(objects[key])

    def do_update(self, usr_in):
        _input = usr_in.split()
        switch = 0
        switch1 = 0
        objects = storage.all()
        if _input[0] not in class_check:
            print("** class doesn't exist **")
        elif len(_input) < 2:
            num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for letter in _input[0]:
                if letter in num_list:
                    switch1 = 1
            if switch1 == 1:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        elif len(_input) < 3:
            print("** attribute name missing **")
        elif len(_input) < 4:
            print("** value missing **")
        elif len(_input) == 4:
            for key in objects.keys():
                if _input[1] == key:
                    objects[key].__dict__[_input[2]] = _input[3]
                else:
                    objects[key].__dict__ = ({_input[2]: _input[3]})
                storage.save()
                storage.reload()
    #################
    # Help Functions#
    #################

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

    def help_create(self):
        print("Usage: create <valid class name>")

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")

if __name__ == "__main__":
    class_check = {"Amenity": Amenity, "BaseModel": BaseModel,
                   "City": City, "Place": Place, "Review": Review,
                   "State": State, "User": User}
    HBNBCommand().cmdloop()
