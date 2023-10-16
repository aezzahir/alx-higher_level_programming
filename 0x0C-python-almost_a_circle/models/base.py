#!/usr/bin/python3
"""
Module for Base class.
"""

import json
import csv


class Base:
    """
    Base class for managing id attribute.

    Attributes:
        __nb_objects (int): Private class attribute to keep track
        of the number of instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of the Base class.

        Args:
            id (int, optional): An integer identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        list_of_obj = [obj.to_dictionary() for obj in list_objs]
        my_list = cls.to_json_string(list_of_obj)
        with open("{}.json".format(cls.__name__), mode="w") as file:
            file.write(my_list)

    @staticmethod
    def from_json_string(json_string):
        """Return the list from the JSON string representation."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set based on the
        dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        try:
            with open("{}.json".format(cls.__name__), mode="r") as file:
                dics = cls.from_json_string(file.read())
                my_list = [cls.create(**dic) for dic in dics]
                return my_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize data to a CSV file."""
        with open("{}.csv".format(cls.__name__), "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    my_list = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    writer.writerow(my_list)
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize data from a CSV file and return a list of instances."""
        try:
            with open("{}.csv".format(cls.__name__), "r", newline="") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(
                            id=int(row[0]),
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4]),
                        )
                    elif cls.__name__ == "Square":
                        instance = cls.create(
                            id=int(row[0]),
                            size=int(row[1]),
                            x=int(row[2]),
                            y=int(row[3]),
                        )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
