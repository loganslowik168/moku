# Base module to be inherited by all Moku modules
class MokuModule:
    NAME = "Base Moku Module"
    MODULE_CONFLICTS = []
    SYSTEM_MESSAGE = []

    def Run(self):
        raise NotImplementedError("All plugins must, at minimum, implement the Run() method.")