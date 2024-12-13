from MokuModule import MokuModule

class HatsuneMiku(MokuModule):
    NAME = "Hatsune Miku"
    conflicts = {}
    SYSTEM_MESSAGES = "You are Hatsune Miku."

    def Run(self):
        print(f"Module {self.NAME} is now running!")