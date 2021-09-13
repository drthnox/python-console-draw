import shlex
from abc import ABCMeta, abstractmethod
import logging

from ConsoleDraw import Canvas
from ConsoleDraw import Drawable

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

class Command(metaclass=ABCMeta):
  def __init__(self, *params):
    pass

  def _execute(self, canvas):
    return canvas

class UnknownCommand(Command):
  def _execute(self, canvas):
    pass

class DrawLineCommand(Command):

  def __init__(self, *params):
    if len(params) != 4:
      raise ValueError("Invalid number of arguments")
    self.x1=params[0]
    self.y1=params[1]
    self.x2=params[2]
    self.y2=params[3]

  def _execute(self, canvas):
    canvas.add(Drawable.Line(canvas,self.x1,self.y1,self.x2,self.y2))
    return canvas

class QuitCommand(Command):
  pass
class CreateCanvasCommand(Command):
  rows = 1
  columns = 1

  def __init__(self, *params):
    if len(params[0]) != 2:
      raise ValueError("Invalid number of arguments")
    self.columns = int(params[0][0])
    self.rows= int(params[0][1])

  def _execute(self, canvas=None):
    return Canvas.Canvas(width=self.columns, height=self.rows)

class CommandFactory:

  def _get_command(instruction):
    commandAndParams = shlex.shlex(instruction)
    commandAndParams.whitespace_split = True
    command = list(commandAndParams)
    logging.debug('command: %s', str(command))
    cmd = command[0].lower()
    if cmd == 'c' or cmd == 'create':
        return CreateCanvasCommand(command[1:])
    elif cmd == 'l' or cmd == 'line':
        return DrawLineCommand(command[1:])
    elif cmd == 'q' or cmd == 'quit':
      return QuitCommand()
    else:
      logging.error('Unknown command')
    return UnknownCommand()
