from abc import ABC, abstractmethod

from ctcl.commons.step_input import StepInput
from ctcl.commons.step_output import StepOutput


class ISolution(ABC):

    @abstractmethod
    def set_step_input(self, step_input: StepInput):
        pass

    class IBruteForce(ABC):
        @abstractmethod
        def bruteforce(self):
            pass

    class ITimeOptimized(ABC):
        @abstractmethod
        def time_optimization(self):
            pass

    class ISpaceOptimized(ABC):
        @abstractmethod
        def space_optimization(self):
            pass

    class IMiscellaneous(ABC):
        @abstractmethod
        def miscellaneous(self):
            pass

    @abstractmethod
    def get_step_output(self) -> StepOutput:
        pass
