from abc import abstractmethod
from enum import Enum
import re


class Tag:
    @abstractmethod
    def match(self, verify_tag):
        pass
    # verify if this method is necessary for this project

    @abstractmethod
    def validateTag(self):
        pass


class NormalTag(Tag):

    def match(self, verify_tag):
        if verify_tag.isalpha():
            return True
        return False

    def validateTag(self, verify_tag):
        return verify_tag.isalpha()


class AddCommandTag(Tag):

    def match(self, verify_tag):
        exp_re = "^([a-zA-Z0-9],?)+$"
        if re.search(exp_re, verify_tag):
            return True
        return False

    def validateTag(self):
        pass


class AddTag(Tag):

    def match(self, verify_tag):
        if verify_tag[0] == "+" and verify_tag[1:].isalpha():
            return True
        return False

    def validateTag(self, verify_tag):
        pass


class SubtractionTag(Tag):

    def match(self, verify_tag):
        if verify_tag[0] == "+" and verify_tag[1:].isalpha():
            return True
        return False

    def validateTag(self):
        pass


class ValidateTag(Enum):
    NormalTag = (1, NormalTag())
    AddCommandTag = (2, AddCommandTag())
    AddTag = (3, AddTag())
    SubtractionTag = (4, SubtractionTag())

    def __init__(self, code, tag_instance):
        self.code = code
        self.tag_instance = tag_instance

    @staticmethod
    def match_tag(find_tag):
        for tag in ValidateTag:
            if tag.tag_instance.match(find_tag):
                return tag.tag_instance
        raise ValueError("The tag value is invalid")