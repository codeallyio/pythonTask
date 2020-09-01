# You can use below packages, but you don't have to. Remember that to use other packages
# you will presumably need to install it manually.

import sys
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print("Too few arguments, need at least url")
        sys.exit(1)

    # TODO complete this program
