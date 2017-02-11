#!/usr/bin/python3
"""
Entry point to the command interpreter.
"""
import cmd
from models.__init__ import storage
from models.base_model import BaseModel


class Console(cmd.Cmd):
    """
    Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    Avoid execution of the user just presses enter as well.
    """
    #################
    # Do Commands ###
    #################
    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return False

    def do_create(self, user_input):
        """Creates a new instance and returns the unique id"""
        input_len = user_input.split()
        if (input_len):
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
            storage.reload()
        else:
            print("Please specify an instance to be created.")

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
                    print (objects[key])
            else:
                print (objects[key])

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

if __name__ == "__main__":
    class_check = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]
    prompt = Console()
    prompt.prompt = "(hbnb) "
    prompt.emptyline
    prompt.cmdloop()
