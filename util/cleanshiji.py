import codecs
fr=codecs.open("/mnt/24shi/01_史记.txt","r","utf-8")
fw=codecs.open("/mnt/24shi/01_史记c.txt","w","utf-8")
for line in fr:
    line=line.strip()
    if not line:
        continue
    if line.startswith("注"):
        continue
    line=line.replace("①","").replace("②","").replace("③","").replace("④","").replace("⑤","").replace("⑥","")
    fw.write(line)
    fw.write('\n')