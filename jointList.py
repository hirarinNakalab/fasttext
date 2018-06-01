import glob
import os

for f in glob.glob("./*.lst"):
    os.system("cat "+f+" >> label_negaposi.lst")