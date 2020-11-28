from todo.views import Views
import re
from todo.validatorParam import ValidatorParameter
VIEW = Views()

class Command_Generate:
    def get_command(self, chain_text):
        separation_commands = chain_text.split()
        response = {
            "status": False,
            "id": None,
            "filters": [],
            "command": "",
            "description": "",
            "parameters": []
        }
        try:
            if not chain_text:
                raise ValueError(chain_text)
            if separation_commands[0] != "todo":
                raise ValueError(chain_text)
            del separation_commands[0]
            finish_filters = False
            exist_description = False
            for value in separation_commands:
                if not finish_filters:
                    # command separation is here (value in commands)
                    if ValidatorParameter.exists(value):
                        finish_filters = True
                        response["command"] = value
                    else:
                        #this is the new change in solution for this task
                        if value.isdigit():
                            response["id"] = int(value)
                        else:
                            if value.startswith("+"):
                                response["filters"].append(tuple(['tag', value[1:]]))
                            else:
                                x = self.join_command(response["filters"], value)
                                response["filters"] = x
                else:
                    if response["command"] == "add" or response["command"] == "modify":
                        if not exist_description:
                            if value.startswith('"') and value.endswith('"'):
                                exist_description = False
                                response["description"] += value[1:len(value) - 1]
                            else:
                                if value[0] == '"':
                                    exist_description = True
                                    response["description"] += value[1:len(value) + 1]
                                else:
                                    if value.startswith("+") or value.startswith("-"):
                                        response["parameters"].append(tuple(["tag", value]))
                                    else:
                                        x = self.join_command(response["parameters"], value)
                                        response["parameters"] = x
                        else:
                            if value[len(value) - 1] == '"':
                                exist_description = False
                                response["description"] += " {}".format(value[0:len(value) - 1])
                            else:
                                response["description"] += " {}".format(value)
                    else:
                        if value.startswith("+") or value.startswith("-"):
                            response["parameters"].append(tuple(["tag", value]))
                        else:
                            x = self.join_command(response["parameters"], value)
                            response["parameters"] = x
        except ValueError as e:
            print("Error: {}".format(e))
        finally:
            return response

    def join_command(self, param, value):
        if re.search("^((.+):(.+)){2}$", value) or re.search("^[A-Za-z0-9]+$", value):
            new_param = list(param[-1])
            new_param[1] = new_param[1] + " {}".format(value)
            param[-1] = tuple(new_param)
        else:
            param.append(tuple(value.split(":")))
        return param

class Controller:
    """
    Class for actions controller
    """
    COMMAND = Command_Generate()
    def run(self):
        """
        Run Application
        :return:
        """
        should_exit = False
        while not should_exit:
            command = VIEW.show_menu()
            if command == "exit":
                should_exit = True
            else:
                print(self.COMMAND.get_command(command))


if __name__ == "__main__":
    command = Command_Generate()
    txt = 'todo +r add "Hello world" +r -df hola:hola mundo'
    print(command.get_command(txt))