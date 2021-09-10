from abc import ABCMeta, abstractmethod


class AbstractCommand(metaclass=ABCMeta):
  def __init__(self):
    pass

  @abstractmethod
  def execute(self):
    pass

class UnknownCommand(AbstractCommand):
  def execute(self):
    pass

class DrawLineCommand(AbstractCommand):
  def execute(self):
    pass

class CommandFactory:
  def _get_command(instruction):
    cmd = str(instruction).lower().lstrip()
    print("command: " + cmd)
    if cmd == 'u':
      return UnknownCommand()
    elif cmd == "l":
      return DrawLineCommand()
    else:
      raise ValueError(instruction)
