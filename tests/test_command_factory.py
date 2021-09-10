from ConsoleDraw import Commands

def test_create_unknowncommand():
  cmd = Commands.CommandFactory._get_command(instruction="u")
  assert isinstance(cmd, Commands.UnknownCommand)

def test_create_drawlinecommand():
  cmd = Commands.CommandFactory._get_command(instruction="l")
  assert isinstance(cmd, Commands.DrawLineCommand)
