# encoding = utf8
import codecs
import re
fr=codecs.open("/mnt/projectbook/train.txt","r","utf-8")
fw=codecs.open("/mnt/projectbook/projfortrain.txt","w","utf-8")
linecs=[]
for line in fr:
    if not line.strip():
        continue
    #line=re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]').sub(' ', line)
    linec=line.replace("["," ").replace("]","/proj ")
    linecs.append(linec)
for line in linecs:
    words=line.split()
    for word in words:
        if word.find("/proj")==-1:
            for char in word:
                fw.write(char+" O")
                fw.write("\n")
                if char=="。" or char =="？" or char=="！":
                    fw.write("\n")
        else:
            if word.find("、")!=-1 or word.find("。")!=-1:
                continue
            word=word.split("/")[0]
            if not word.strip():
                continue
            if len(word) > 1:
                fw.write(word[0] + ' ' + 'B-' + "proj" + '\n')
                # 词中间的字
                for char in word[1:(len(word) - 1)]:
                    fw.write(char + ' ' + 'I-' + "proj" + '\n')
                # 词的尾字
                fw.write(word[-1] + ' ' + 'E-' + "proj" + '\n')
                # 单字词
            else:
                fw.write(word + ' ' + 'S-' + "proj " + '\n')
    fw.write("\n")