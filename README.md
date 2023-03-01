### :/

```
# MUST INSTALLpip install lolcat

from subprocess import (
    run
)


def lolcat(text):
  run(["lolcat"], input=text, text=True)

logo = """


  ██████    ██     █████      ███    ███
 ██         ██    ██   ██     ████  ████
  █████     ██    ███████     ██ ████ ██
      ██    ██    ██   ██     ██  ██  ██
 ██████     ██    ██   ██     ██      ██

"""

lolcat(logo)
```
