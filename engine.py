class Engine:
    def __init__(self):
        self.__started = False

    def start(self):
        self.__started = True

    def stop(self):
        self.__started = False
    