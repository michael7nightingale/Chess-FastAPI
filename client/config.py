import json
from collections import UserDict


class Config(UserDict):
    """Config subclass of a dict. Writes any key changes into json file."""
    filename: str = "config.json"

    @classmethod
    def load_config(cls):
        with open(cls.filename) as config_json_file:
            config = json.load(config_json_file)
            return cls(config)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        with open(self.__class__.filename, "w") as config_json_file:
            json.dump(dict(self.items()), config_json_file)

    def __delitem__(self, key):
        super().__delitem__(key)
        with open(self.__class__.filename, "w") as config_json_file:
            json.dump(dict(self.items()), config_json_file)
