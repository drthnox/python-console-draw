from ConsoleDraw import Commands

def test_create_unknowncommand():
  cmd = Commands.CommandFactory._get_command(instruction="u")
  assert isinstance(cmd, Commands.UnknownCommand)

def test_create_createcanvascommand():
  cmdLine = "c 10 10"
  cmd = Commands.CommandFactory._get_command(instruction=cmdLine)
  assert isinstance(cmd, Commands.CreateCanvasCommand)
