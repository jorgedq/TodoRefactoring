from todo.views import Views

VIEW = Views()


class Controller:
    """
    Class for actions controller
    """
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
                print(self.redirect_command(command))

    def redirect_command(self, chain_text):
        """
        redirect to parse command entered
        :param chain_text:
        :return:
        """
        if "add" in chain_text:
            print("comando add introducido")
        if "modify" in chain_text:
            print("comando modify")
        if "list" in chain_text:
            print("comando list")
        if "done" in chain_text:
            print("command done")
        if "start" in chain_text:
            print("the command start")