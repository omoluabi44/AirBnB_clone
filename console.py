#!/usr/bin/python3
""" my arbnd console module """

import re
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return ret1

class HBNBCommand(cmd.Cmd):
    """
    class for airbnd console
    """

    prompt = "(hbnb) "
    class_instances = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        exit the cmd when press ctr-d
        """
        print("")
        return True

    def emptyline(self):
        """
        do nothing when no command is input

        """
        pass

    def do_create(self, line):
        """
        Create a new instance of specified class
        Usage: <command> <class>
        """
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name in self.class_instances:
            new_instance = self.class_instances[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        show a new instance of specified class
        Usage: <command> <class>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_instances:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance_key])

    def do_destroy(self, line):
        """
        destroy an instance of specified class
        Usage: <command> <class>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_instances:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        all_obj_key = storage.all()
        delete_key = "{}.{}".format(class_name, instance_id)
        if delete_key not in all_obj_key:
            print("** no instance found **")
            return
        del all_obj_key[delete_key]
        storage.save()

    def do_all(self, line):
        """
        show all instance or instance of specified class
        Usage: <command> <class> or <command>
        """
        if not line:
            all_objs = storage.all().values()
            all = []
            for obj in all_objs:
                all.append(obj.__str__())
            print(all)
        else:
            class_name = line.split()[0]
            if class_name not in self.class_instances:
                print("** class doesn't exist **")
                return
            tmp_class_name = []
            all_class = storage.all().values()
            for obj in all_class:
                if obj.__class__.__name__ == class_name:
                    tmp_class_name.append(obj.__str__())
            print(tmp_class_name)

    def do_update(self, line):
        """
        update the class using id
        """
        argl = parse(line)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in self.class_instances:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def default(self, line):
        """
        run unrognized command to perform some instruction
        Usage: <Class>.<command()>
        """
        line1 = line.split("(")
        command2 = line1[0]
        command = command2.split(".")[1] + "()"
        class_name = line.split('.')[0]
        if class_name not in self.class_instances:
            print("** class doesn't exist **")
            return
        if command.endswith("all()"):
            instances_and_count = storage.get_intances_by_class(
                class_name)
            instances = instances_and_count[0]
            instances_count = instances_and_count[1]
            j = 0
            if instances:
                print("[", end="")
                for i in instances:
                    j += 1
                    if j < instances_count:
                        print("{}, ".format(i), end="")
                    else:
                        print("{}".format(i), end="")
                print("]")
                print(j)
        elif command.endswith("count()"):
            instances_and_count = storage.get_intances_by_class(
                class_name)
            instances_count = instances_and_count[1]
            if instances_count:
                print(instances_count)
        elif command.endswith("show()"):
            instances_id = line.split("(")[1].split(")")[0][1:-1]
            instances2_id = "{}.{}".format(class_name, instances_id)
            if instances2_id not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[instances2_id])
        elif command.endswith("destroy()"):
            instances_id = line.split("(")[1].split(")")[0][1:-1]
            instances2_id = "{}.{}".format(class_name, instances_id)
            if instances2_id not in storage.all():
                print("** no instance found **")
                return
            del (storage.all()[instances2_id])
            storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
