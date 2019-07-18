import sys
from src.wrapper import wrap

def launch():
    wrap(sys.argv[1:])

if __name__ == "__main__":
    launch()
