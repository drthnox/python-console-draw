import shlex
from abc import ABCMeta, abstractmethod
import logging

from ConsoleDraw import Canvas

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

class Drawable(metaclass=ABCMeta):
  def __init__(self, *params):
    pass

  def draw(self, canvas):
    pass

class Line(Drawable):

  def __init__(self, *params):
    super().__init__()
    self.row1 = params[0]
    self.col1 = params[1]
    self.row2 = params[2]
    self.col2 = params[3]

  def is_valid(self):
    return self.row1 == self.row2 or self.col1 == self.col2

  def draw(self, canvas):
    r1 = self.row1
    r2 = self.row2
    c1 = self.col1
    c2 = self.col2
    if self.row1 < 0:
        r1 = 0
    if self.row2 < 0:
        r2 = 0
    if r1 > canvas.height:
        r1 = canvas.height
    if r2 > canvas.height:
        r2 = canvas.height
    if self.col1 < 0:
        c1 = 0
    if self.col2 < 0:
        c2 = 0
    if c1 > canvas.width:
        c1 = canvas.width
    if c2 > canvas.width:
        c2 = canvas.width
    for row in range(0, abs(r1-r2)+1):
        for col in range(0, abs(c1-c2)+1):
            canvas.pixels[row,col] = 1
    return canvas
