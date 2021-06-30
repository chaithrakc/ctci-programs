from abc import ABC, abstractmethod


class ILinkedList(ABC):
    head = None

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def len(self) -> int:
        pass

    @abstractmethod
    def insert(self, index, data) -> bool:
        pass

    @abstractmethod
    def append_head(self, data) -> bool:
        pass

    @abstractmethod
    def append_tail(self, data) -> bool:
        pass

    @abstractmethod
    def remove(self, data) -> bool:
        pass

    @abstractmethod
    def remove_head(self):
        pass

    @abstractmethod
    def remove_tail(self):
        pass

    @abstractmethod
    def find(self, data) -> int:
        pass
