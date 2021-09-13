import shlex

from ConsoleDraw.Canvas import Canvas
from ConsoleDraw.Commands import CommandFactory, QuitCommand
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

def main():
  canvas = Canvas()
  quit = False
  while quit == False:
    instruction = str(input('Enter Command:> ')).lower().strip(' ')
    command = CommandFactory._get_command(instruction)
    logging.debug("command: %s", str(type(command)))
    if isinstance(command, QuitCommand):
      quit = True
    else:
      command._execute(canvas)

if __name__ == '__main__':
  main()
