# -*- coding: utf-8 -*-
import re
import os
import sys
import fasttext as ft
import subprocess as cmd

INPUT_VALI_DIR = './threeclass/valid/'
ENC_CONFIG = 'utf-8'

classifier = ft.load_model('fixedthreeclassification.bin')

def get_all_files(in_dir):
    for root, dirs, files in os.walk(in_dir):
        for file in files:
            yield os.path.join(root, file)

def read_document(path, encoding):
    with open(path, 'r', encoding=encoding, errors='ignore') as f:
        return f.read()
    
def corpus_to_sentences(corpus, encoding):
    docs = [read_document(x, encoding) for x in corpus]
    for idx, (doc, name) in enumerate(zip(docs, corpus)):
        yield split_into_words(doc, name)
        
def trim_doc(doc):
    lines = doc.splitlines()
    valid_lines = []
    for line in lines:
        line = re.sub(r'[＜＞]', ' ', line) #正規表現置換
        line = re.sub(r'^F\d\d\d：', '', line)
        line = re.sub(r'Ｘ：', '', line)
        line = re.sub(r'^M\d\d\d：', '', line)
        if line.startswith('＠'):
            continue
        if line == '':
            continue
        if line.startswith('％'):
            continue
        valid_lines.append(line) #別リストにする
    return valid_lines

def split_into_words(doc, name=''):
    valid_doc = trim_doc(doc)
    
    daily_prob = 0
#     houhan_prob = 0
    low_prob = 0
    mid_prob = 0
    high_prob = 0

    print(name)
    for document in valid_doc: 
        morp = cmd.getstatusoutput("echo " + document + " | mecab -Owakati -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
        words = morp[1]
        estimate = classifier.predict([words], k=4)
        estimate_2 = classifier.predict_proba([words], k=4)
        if estimate[0][0] == "__label__1,":
            low_prob += estimate_2[0][0][1]
        elif estimate[0][0] == "__label__2,":
            mid_prob += estimate_2[0][0][1]
        elif estimate[0][0] == "__label__3,":
            high_prob += estimate_2[0][0][1]
        elif estimate[0][0] == "__label__0,":
            daily_prob += estimate_2[0][0][1]   
#     return (name, daily_prob, low_prob, mid_prob, high_prob)
    return (name, daily_prob, low_prob, mid_prob, high_prob)


corpus = list(get_all_files(INPUT_VALI_DIR))
sentences = list(corpus_to_sentences(corpus, ENC_CONFIG))