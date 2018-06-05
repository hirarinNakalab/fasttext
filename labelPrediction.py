# -*- coding: utf-8 -*-
import sys
import fasttext as ft
import subprocess as cmd

obj = sys.argv[1]
morp = cmd.getstatusoutput("echo " + obj + " | mecab -Owakati -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
words = morp[1]
print('\n', words)

classifier = ft.load_model('multi.bin')
estimate = classifier.predict([words], k=4)
estimate_2 = classifier.predict_proba([words], k=4)

print(estimate[0])
if estimate[0][0] == "__label__1,":
    print('日常会話',estimate_2[0][0][1])
elif estimate[0][0] == "__label__2,":
    print('危険度低',estimate_2[0][0][1])
elif estimate[0][0] == "__label__3,":
    print('危険度中',estimate_2[0][0][1])
elif estimate[0][0] == "__label__4,":
    print('危険度高',estimate_2[0][0][1])   