# coding=utf-8
import codecs
import os
import random



def eachFile(filepath):
    pathls = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        pathls.append(child)
    return pathls


def pretrain(path):
    fr = codecs.open(path, 'r', 'utf-8')
    fw = codecs.open(path.split('.')[0] + 'ed.txt', 'w', 'utf-8')
    for line in fr:
        print(line)


def dataclean():
    trainsents = []
    valsents = []
    fr = codecs.open('/mnt/corpus/zm.xml', 'r', 'utf-8')
    fw = codecs.open('/mnt/zmtrain.txt', 'w', 'utf-8')
    for line in fr:
        line = line.replace("<专名>", " ").replace("</专名>", "/zm ").replace("<书名>", " ").replace("</书名>", "/sm ")
        fw.write(line)
def gettrainval():
    fr= codecs.open('/mnt/zmtrain.txt', 'r', 'utf-8')
    fw = codecs.open('/mnt/zmfortrain.txt', 'w', 'utf-8')
    fw1  =codecs.open('/mnt/zmfortest.txt', 'w', 'utf-8')
    num=0
    wxs=[]
    for line in fr:
        wxs.append(line)
    random.shuffle(wxs)
    for line in wxs:
        if line.find("<正文>")==-1:
            continue
        line=line.replace("<正文>","")
        line = line.replace("</正文>", "")
        words=line.split()
        for word in words:
            if word.find("/zm")!=-1:
                word=word.split("/")[0]
                if len(word) > 1:
                    fw.write(word[0] + ' ' + 'B-' + "zm" + '\n')
                    # 词中间的字
                    for char in word[1:(len(word) - 1)]:
                        fw.write(char + ' ' + 'I-' + "zm" + '\n')
                    # 词的尾字
                    fw.write(word[-1] + ' ' + 'E-' + "zm" + '\n')
                    # 单字词
                else:
                    fw.write(word + ' ' + 'S-' + "zm" + '\n')
            elif word.find("/sm")!=-1:
                word = word.split("/")[0]
                if len(word) > 1:
                    fw.write(word[0] + ' ' + 'B-' + "sm" + '\n')
                    # 词中间的字
                    for char in word[1:(len(word) - 1)]:
                        fw.write(char + ' ' + 'I-' + "sm" + '\n')
                    # 词的尾字
                    fw.write(word[-1] + ' ' + 'E-' + "sm" + '\n')
                    # 单字词
                else:
                    fw.write(word + ' ' + 'S-' + "sm" + '\n')
            else:
                sentnum=0
                for char in word:
                    sentnum+=1
                    fw.write(char+' O'+'\n')
                    if (char == '。' or char == '？' or char == '！'):
                        # if sentnum>100:
                        #     print(sentnum)
                        sentnum=0
                        fw.write('\n')
        num+=1
        print(num)
        if num==7670:
            fw=fw1
if __name__ == "__main__":
    gettrainval()
    #dataclean()
    # pretrain('/mnt/corpus/yuanshi/元史-001-235545.xml')
