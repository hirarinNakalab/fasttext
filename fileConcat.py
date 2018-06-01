import glob
import os

for f in glob.glob("./nucc/out/data*.txt"):
    os.system("cat "+f+" >> negative.txt")