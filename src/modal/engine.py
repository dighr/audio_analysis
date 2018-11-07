
class Engine:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Engine.__instance is not None:
            raise Exception("This class is a singleton! Call the instance methods")
        else:
            Engine.__instance = self

    @staticmethod
    def get_instance():
        if Engine.__instance is None:
            Engine.__instance = Engine()
        return Engine.__instance

    def get_name(self):
        return self.__name

