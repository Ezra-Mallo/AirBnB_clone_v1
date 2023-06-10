#!/usr/bin/env python3


import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point of the command interpreter:
    """

    # intro = 'Welcome to hbnb shell.\n'
    prompt = "(hnbn) "
    __classes = {
            'BaseModel': BaseModel
            }

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to JSON file) and 
        prints the id. Ex: $ create BaseModel
        """
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance =  HBNBCommand.__classes[arg]()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)


    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        myArgs = arg.split()
        if len(myArgs) == 0:
            print("** class name missing **")
        elif myArgs[0] not in HBNBCommand.__classes:
                print("** class doesn't exist ** ")
        elif len(myArgs) < 2:
            print("** instance id missing **")
        else:
            class_name =  myArgs[0]
            instance_id =  myArgs[1]

            Key = "{}.{}".format(class_name, instance_id)
            class_instance = storage.all()

#            print("key {}".format(key))
#            print("Instance {}".format(class_instance))
            if key in class_instance:
                print(class_instance[key])
            else:
                print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
