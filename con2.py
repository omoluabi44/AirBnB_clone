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
            if instances:
                print("[", end="")
                for i in instances:
                   print(i, end="")
                print("]")
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
            del (models.storage.all()[instances2_id])
            storage.save()
        elif command.endswith("update()"):
            instances_id = line.split()
            instances_id = line.split("(")[1].split(")")[0][1:]
            id = instances_id.split(",")[0][:-1]
            attr_name = instances_id.split(",")[1][2:-1]
            attr_value = instances_id.split(",")[2]
            key = "{}.{}".format(class_name, id)
            all_obj = storage.all()
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
                    storage.save()
                except ValueError:
                    print("** value missing **")
                else:
                    setattr(obj, attr_name, attr_value)
                    storage.save()
            else:
                print("*** Unknown syntax: {} ".format(line))
