from MokuModule import MokuModule

class HatsuneMiku(MokuModule):
    NAME = "Hatsune Miku"
    conflicts = {}
    SYSTEM_MESSAGE = "You are Hatsune Miku."
    ASSISTANT_NAME = "Miku"

    def Run(self):
        print(f"Module {self.NAME} is now running!")