import glob
import os

for f in glob.glob("./multiclass/train/*.lst"):
    os.system("cat "+f+" >> ./multiclass/train/label_multi.lst")