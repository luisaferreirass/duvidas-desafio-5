from typing import Dict
from abc import ABC, abstractmethod

class PJListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
