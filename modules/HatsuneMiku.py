from MokuModule import MokuModule

class HatsuneMiku(MokuModule):
    NAME = "Hatsune Miku"
    conflicts = {}
    
    def Run(self):
        print(f"MODULE {self.NAME} IS NOW RUNNING!")