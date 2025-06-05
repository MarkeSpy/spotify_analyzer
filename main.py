import sys
import os
sys.path.append(os.path.abspath("./src"))

from spotify_analyzer.data import *

xynw = lela("short_term")
print(xynw)