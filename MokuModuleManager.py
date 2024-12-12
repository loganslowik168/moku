# Module manager for all Moku modules
import importlib
from pathlib import Path

from MokuModule import MokuModule


class MokuModuleManager:
    def __init__(self, modulesDirectory):
        self.modulesDirectory = modulesDirectory
        self.modules = {}

    # Loads all modules in a specified folder
    def LoadModules(self):
        moduleFiles = Path(self.modulesDirectory).glob("*.py")
        print(f"Checking directory {Path(self.modulesDirectory).resolve()} for any modules.")
        for file in moduleFiles:
            moduleName = file.stem
            module = importlib.import_module(f"modules.{moduleName}")
            for attribute in dir(module):
                attr = getattr(module, attribute)
                try:
                    print(f"Detected module: {attr.NAME}")
                except:
                    pass

                if isinstance(attr, type) and issubclass(attr, MokuModule) and attr is not MokuModule:
                    self.modules[attr.NAME] = attr()

    def CheckModuleConflicts(self, modules):
        for m in modules:
            module = self.modules.get(m)
            if not module:
                raise ValueError(f"Module {m} not found!")
            for conflict in module.conflicts:
                if conflict in modules:
                    raise ValueError(f"Conflict detected: {m} conflicts with {conflict}")

    def RunModules(self, modules):
        for m in modules:
            module = self.modules[m]
            module.Run()