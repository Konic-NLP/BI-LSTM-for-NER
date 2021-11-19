import os
import codecs
sentlen={}
bdfh = {"。", "！", "？", "，", "；", "、", "：", ",", "；"}
for filename in os.listdir('/mnt/24shi'):
    print (filename)
    fr=codecs.open("/mnt/24shi/"+filename, "r", "gb18030")
    charnum=0
    bdnum=0
    chars={}
    for line in fr:
        line=line.strip()
        if not line:
            continue
        for char in line:
            charnum+=1
            if char in bdfh:
                bdnum+=1
        for i,char in enumerate(line[:-1]):
            if line[i+1] in bdfh:
                if char in chars.keys():
                    chars[char]=chars[char]+1
                else:
                    chars[char]=1
    charls=sorted(chars.items(),key=lambda  item:item[1],reverse=True)
    for char in charls[:10]:
        print(char)
    print(charnum)
    print(bdnum)
    print(charnum/bdnum)
    sentlen[filename]=charnum/bdnum
