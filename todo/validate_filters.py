from abc import abstractmethod
from enum import Enum


# change the name


class ValidateFilters():
    @abstractmethod
    def validate(self):
        pass


class TagValidate(ValidateFilters):
    def validate(self):
        pass


class ValidationFilters(Enum):
    TAG = (1, TagValidate())
