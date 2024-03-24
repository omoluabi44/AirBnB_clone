#!/usr/bin/python3
""" my arbnd console module """


import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    class_instances = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """
        init my console
        """

        super().__init__()
        self.prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        print()
        """
        exit the cmd when press ctr-d

        """
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
        if instance_key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[instance_key])

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
        all_obj_key = models.storage.all()
        delete_key = "{}.{}".format(class_name, instance_id)
        if delete_key not in all_obj_key:
            print("** no instance found **")
            return
        del all_obj_key[delete_key]
        models.storage.save()

    def do_all(self, line):
        """
        show all instance or instance of specified class
        Usage: <command> <class> or <command>
        """
        if not line:
            all_objs = models.storage.all().values()
            for obj in all_objs:
                print([str(obj)])
        else:
            class_name = line.split()[0]
            if class_name not in self.class_instances:
                print("** class doesn't exist **")
                return
            tmp_class_name = []
            all_class = models.storage.all().values()
            for obj in all_class:
                if obj.__class__.__name__ == class_name:
                    tmp_class_name.append(obj)
            for i in tmp_class_name:
                print([str(i)])

    def do_update(self, line):
        """
        update a  instance of specified class
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
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_obj = models.storage.all()

        if key not in all_obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        obj = all_obj[key]
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            try:
                setattr(obj, attribute_name, attr_type(attribute_value))
                models.storage.save()
            except ValueError:
                print("** value missing **")
        else:
            setattr(obj, attribute_name, attribute_value)
            models.storage.save()

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
        if command.endswith("all()")
        instances_and_count = models.storage.get_intances_by_class(class_name)
        instances = instances_and_count[0]
        if instances:
            print("[", end="")
            for i in instances:
                print(i, end="")
                print("]")
        elif command.endswith("count()"):
            instances_and_count = models.storage.get_intances_by_class(class_name)
            instances_count = instances_and_count[1]
            if instances_count:
                print(instances_count)
        elif command.endswith("show()"):
            instances_id = line.split("(")[1].split(")")[0][1:-1]
            instances2_id = "{}.{}".format(class_name, instances_id)
            if instances2_id not in models.storage.all():
                print("** no instance found **")
                return
            print(models.storage.all()[instances2_id])
        elif command.endswith("destroy()"):
            instances_id = line.split("(")[1].split(")")[0][1:-1]
            instances2_id = "{}.{}".format(class_name, instances_id)
            if instances2_id not in models.storage.all():
                print("** no instance found **")
                return
            del (models.storage.all()[instances2_id])
            models.storage.save()
        elif command.endswith("update()"):
            instances_id = line.split()
            instances_id = line.split("(")[1].split(")")[0][1:]
            id = instances_id.split(",")[0][:-1]
            attr_name = instances_id.split(",")[1][2:-1]
            attr_value = instances_id.split(",")[2]
            key = "{}.{}".format(class_name, id)
            all_obj = models.storage.all()
            if key not in all_obj:
                print("** no instance found **")
                return
            obj = all_obj[key]
            if hasattr(obj, attr_name):
                c_d = getattr(obj, attr_name)
                attr_type = type(c_d)
                try:
                    n_v = attr_type(attr_value)
                    setattr(obj, attr_name, n_v)
                    models.storage.save()
                except ValueError:
                    print("** value missing **")
                else:
                    setattr(obj, attr_name, attr_value)
                    models.storage.save()
            else:
                print("*** Unknown syntax: {} ".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
