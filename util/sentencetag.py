#古文断句预处理
import codecs
def removepos():
    fr=codecs.open("/mnt/zzjudou.txt","r","utf-8")
    fw=codecs.open("/mnt/zzforjudou.txt","w","utf-8")
    num=0
    for line in fr:
        num += 1
        if not line.split():
            continue
        wordtags=line.split()

        for wordtag in wordtags:
            print(wordtag)
            print(num)
            word,tag=wordtag.split("/")
            fw.write(word)
        fw.write("\n")
def senttag():
    fr = codecs.open("/mnt/han.txt", "r", "utf-8")
    fw = codecs.open("/mnt/hantrain.txt", "w", "utf-8")
    sentnum=0
    maxchars=0
    charnum=1
    linenum=0
    bdfh={"。","！","？","，","；","、","“","”", "：","‘",",","’","-","—","「","」","』","『","；","〔","〕"}
    middle = {"，","；","、","：","；"}
    end = {"。","！","？"}
    for line in fr:
        line=line.strip()
        if len(line)<=11:
            continue

        if line[-1] not in bdfh:
            continue
        linenum+=1
        #print(linenum)
        sentchars=0
        for i,char in enumerate(line[:-1]):
            if not char.strip():
                continue
            if char in bdfh:
                continue
            charnum+=1
            sentchars+=1
            if line[i+1] in end:
                fw.write(char+" S-end")
                sentnum += 1
                if sentnum == 20:
                    if maxchars < charnum:
                        maxchars = charnum
                    charnum = 0
                    sentnum = 0
            elif line[i+1] in middle:
                sentchars = 0
                fw.write(char+" S-end")
                sentnum += 1
                if sentnum == 20:
                    if maxchars < charnum:
                        maxchars = charnum
                    charnum = 0
                    sentnum = 0
                    fw.write("\n")
            else:
                fw.write(char + " O")
            fw.write("\n")
    print(maxchars)

def clean24():
    fr = codecs.open("/mnt/24shi/23shi.txt", "r", "utf-8")
    fw = codecs.open("/mnt/23shic.txt", "w", "utf-8")
    bdfh = {"。", "！", "？", "，", "；", "、", "“", "”", "：", "‘", ",", "’", "-", "—", "「", "」", "』", "『", "；"}
    for line in fr:
        line = line.strip()
        line = line.replace("？","。")
        if len(line) <= 11:
            continue
        if line[-1] not in bdfh:
            continue
        bigsents=line.split("。")
        for sent in bigsents:
            if len(sent)>100:
                print(sent)

def senttagbychars():
    fr = codecs.open("/mnt/hantest.txt", "r", "utf-8")
    fw = codecs.open("/mnt/hantest50.txt", "w", "utf-8")
    charsnum=0
    for line in fr:
        if not line.strip():
            continue
        word,tag = line.split()
        fw.write(word+" "+tag)
        fw.write('\n')
        charsnum+=1
        if charsnum==50:
            fw.write('\n')
            charsnum=0
if __name__ == "__main__":
    senttag()
    #senttagbychars()