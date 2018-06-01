import codecs
import re

for i in range(129):
    f_in  = codecs.open('./nucc/data{:03d}.txt'.format(i+1), 'r', 'utf-8')
    f_out = codecs.open('./nucc/out/data{:03d}.txt'.format(i+1), 'w', 'utf-8')

    lines = f_in.readlines() #読み込み
    lines2 = []
    for line in lines:
        line = re.sub(r'[＜＞]', ' ', line) #正規表現置換
        line = re.sub(r'^F\d\d\d：', '', line)
        line = re.sub(r'Ｘ：', '', line)
        line = re.sub(r'^M\d\d\d：', '', line)
        if line.startswith('＠'):
            continue
        if line.startswith('％'):
            continue
        lines2.append(line) #別リストにする
    else:
        f_out.write("".join(lines2)) #書き込み
        f_in.close()
        f_out.close()