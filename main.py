from ConsoleDraw.Canvas import Canvas
from ConsoleDraw.CommandFactory import CommandFactory
from ConsoleDraw.AbstractCommand import AbstractCommand
from ConsoleDraw.ExitCommand import ExitCommand
import shlex


def main():
    while True:
        instruction = str(input('Enter Command:> ')).lower().strip(' ')
        command = parse(instruction)
        if command.type() != QUIT:
            command.exeute()
        else:
            print('Thank you!')
            break


def parse(command):
    instruction = shlex.shlex(command)
    instruction.whitespace_split = True
    return CommandFactory.createCommand(instruction)

if __name__ == '__main__':
    main()
