import glob
import os

for f in glob.glob("./threeclass/train/fixed*.lst"):
    os.system("cat "+f+" >> ./threeclass/train/fixedlabel_threeclass.lst")