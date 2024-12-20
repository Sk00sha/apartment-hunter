from abc import ABC, abstractmethod

class StepRunner(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def save(self):
        pass

