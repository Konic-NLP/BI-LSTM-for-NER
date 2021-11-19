# coding=utf-8
import logging
import os.path
import sys
import codecs
import gensim
import multiprocessing

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))


class MySentences(object):
    temp = []
    num = 0

    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in codecs.open(os.path.join(self.dirname, fname), 'r', 'utf-8'):  #
                '''self.num+=1
                print self.num'''
                '''if line.find('<docno>')!=-1:
                    continue
                if line.find('<url>')!=-1:
                    continue    
                line=line.replace('<contenttitle>','').replace('</contenttitle>','')
                line=line.replace('<content>','').replace('</content>','')
                line=line.replace('<doc>','').replace('</doc>','')'''
                '''for char in line:
                    self.temp.append(char)
                line = ' '.join(self.temp)'''
                chars = []
                line = line.strip()
                if line == '':
                    continue
                else:
                    for char in line:
                        chars.append(char)
                yield chars


sentences = MySentences('/mnt/24shimodel')
print ('读取完毕开始训练。。。。。。')
model = gensim.models.Word2Vec(sentences, workers=multiprocessing.cpu_count(), size=128, window=10, min_count=5)
model.save('/mnt/model/24shi.model')