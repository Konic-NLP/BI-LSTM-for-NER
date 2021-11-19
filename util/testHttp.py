import urllib2
import requests

url = "http://wxsnjnu.iok.la:26597/tagging/servlets/AutoTagServlet"

c = 1
u = urllib2.urlopen(r"file:///C:\Users\DELL\Desktop\1.html")
i = u.read()
##for  i in travel(r"D:\new".decode("utf-8")):

try:

    keywords = {"itext": i}
    r = requests.post(url, data=keywords)
except:
    pass
##res=r.text

##
r = requests.get(url)
res = r.text

f = open("webtest.xml", "w+")
print >> f, res
f.close()