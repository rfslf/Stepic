class LoggableList(Loggable, list):

    def append(self, msg):
        super(LoggableList, self).append(msg)
        self.log(msg)
