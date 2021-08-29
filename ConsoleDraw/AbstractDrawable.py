from abc import ABCMeta, abstractmethod


class AbstractDrawable(metaclass=ABCMeta):

    def __init__(self, canvas):
        self.canvas = canvas
        super().__init__()

    @abstractmethod
    def draw(self):
        pass
