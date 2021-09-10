# from ConsoleDraw import AbstractCommand
from ConsoleDraw import UnknownCommand

class CommandFactory():

  # def __init__(self) -> None:
  #     pass

  def createCommand(self, instruction):
    s = str(instruction)
    c = s.lstrip().lower()
    if c == 'u':
      return UnknownCommand.UnknownCommand(self)