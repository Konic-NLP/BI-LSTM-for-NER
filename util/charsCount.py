import codecs
fr = codecs.open("/mnt/sgz.txt","r","utf-8")
num=0
for line in fr:
    if not line.strip():
        continue
    for char in line:
        print(char)
        if char!=" ":
            num+=1
print(num)