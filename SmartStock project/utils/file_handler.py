import json
import os


class FileHandler:
    """
    Handles reading and writing data
    to JSON files.
    """

    @staticmethod
    def read_json(filename):
        """
        Read data from a JSON file.
        Returns an empty list if the file
        does not exist or contains invalid JSON.
        """

        if not os.path.exists(filename):
            return []

        try:
            with open(filename, "r") as file:
                data = json.load(file)

            return data

        except json.JSONDecodeError:
            return []

    @staticmethod
    def write_json(filename, data):
        """
        Write data to a JSON file.
        """

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def append_json(filename, item):
        """
        Add one new item to a JSON file.
        """

        data = FileHandler.read_json(filename)

        data.append(item)

        FileHandler.write_json(filename, data)