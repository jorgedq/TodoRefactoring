from abc import abstractmethod
from enum import Enum
from tabulate import tabulate


class Validate:
    @abstractmethod
    def validate(self, value):
        pass


class AddValidator(Validate):
    MESSAGE = "The add command is not bad"

    def validate(self, value):
        if value != "hello":
            raise ValueError("no coincide la palabra")


class ValidatorParameter(Enum):
    ADD = (1, AddValidator())

    def __init__(self, code, validator_instance):
        self.code = code
        self.validator_instance = validator_instance

    @staticmethod
    def exists(value):
        for validator in ValidatorParameter:
            if validator.name.lower() == value:
                return True
        return False

    @staticmethod
    def get_validator(validator_name):
        for validator in ValidatorParameter:
            if validator.name.lower() == validator_name:
                return validator.validator_instance
        return None


if __name__ == "__main__":
    validate = ValidatorParameter.get_validator("add")
    try:
        val = validate.validate("hello")

        rios3 = [['Río', 'Long. (Km.)'],
                 ['Almanzora', 105],
                 ['Guadiaro', 79],
                 ['Guadalhorce', 154],
                 ['Guadalmedina', 51.5]]
        print(tabulate(rios3, headers='firstrow', tablefmt='fancy_grid'))
    except ValueError as e:
        print(e)