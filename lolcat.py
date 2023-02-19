# MUST INSTALLpip install lolcat

from subprocess import (
    run
)

logo = """


  ██████    ██     █████      ███    ███
 ██         ██    ██   ██     ████  ████
  █████     ██    ███████     ██ ████ ██
      ██    ██    ██   ██     ██  ██  ██
 ██████     ██    ██   ██     ██      ██

"""

def lolcat(text):
  run(["lolcat"], input=text, text=True)


lolcat(logo)
