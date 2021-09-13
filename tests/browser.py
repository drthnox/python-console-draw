import webbrowser, sys, pyperclip

sys.argv

# check if command line args were passed

if len(sys.argv) > 1:
  # command line args have been passed
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
