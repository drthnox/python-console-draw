from abc import ABCMeta, abstractmethod


class AbstractDrawable(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, canvas):
        pass