from ConsoleDraw.Canvas import Canvas
import shlex


def main():
    while True:
        instruction = str(input('Enter Command:> ')).lower().strip(' ')
        quit = parse(instruction)
        if quit == True:
            break


def parse(command):
    instruction = shlex.shlex(command)
    instruction.whitespace_split = True
    tokenNum = 1
    while True:
        token = instruction.get_token()
        print(str(tokenNum) + ":" + token)
        tokenNum = tokenNum + 1
    return False


if __name__ == '__main__':
    main()
