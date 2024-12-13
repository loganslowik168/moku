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
        errors = []
        i = 0
        while i < len(modules):
            m = modules[i]
            module = self.modules.get(m)
            if not module:
                modules.pop(i)
                errors.append(f"Module {m} not found!")
                continue
            for conflict in module.conflicts:
                if conflict in modules:
                    modules.pop(i)
                    errors.append(f"Conflict detected: {m} conflicts with {conflict}")
                    break
            else:
                i += 1

        raise ValueError("\n".join(errors))

    def RunModules(self, modules):
        systemMessages = []
        print(f"Booting with {len(modules)} modules.")
        for m in modules:
            module = self.modules[m]
            if hasattr(module, 'SYSTEM_MESSAGE'):
                systemMessages.append(module.SYSTEM_MESSAGES)
            module.Run()
        return systemMessages