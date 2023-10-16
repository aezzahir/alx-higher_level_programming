#!/usr/bin/python3
"""
This is the Base Class
"""
import json
import csv


class Base:
    """
    Base class attributes management
    Attributes:
        __nb_objects (int): Private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        Args:
            id (int): An optional integer identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON  representation into a file
        """
        Mylist = []
        for instance in list_objs:
            Mylist.append(instance.to_dictionary())
        json_list = cls.to_json_string(Mylist)
        with open("{}.json".format(cls.__name__), mode="w") as Myfile:
            Myfile.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON representation
        """
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return new attributes
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return list of instance
        """
        filename = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = json.loads(json_data)
                for item in dict_list:
                    instance = cls.create(**item)
                    instances.append(instance)
        except FileNotFoundError:
            return []
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize in CSV
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csvwriter.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csvwriter.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize in CSV
        """
        filename = "{}.csv".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r", newline="") as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4]),
                        )
                    elif cls.__name__ == "Square":
                        instance = cls.create(
                            size=int(row[1]), x=int(row[2]), y=int(row[3])
                        )
                    instance.id = int(row[0])
                    instances.append(instance)
        except FileNotFoundError:
            return []
        return instances
