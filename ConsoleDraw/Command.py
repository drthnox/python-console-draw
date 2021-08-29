from abc import ABC, abstractmethod


class Command():

    @abstractmethod
    def draw(self, canvas):
        pass
