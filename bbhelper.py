import  requests
import  bs4
from login import login
import os
from config import des,headers,host
from download import  download
from os import path
requests.packages.urllib3.disable_warnings()
sBB,rHomePage=login()
bsHomePage=bs4.BeautifulSoup(rHomePage.text,features="lxml")
#print(bsHomePage.prettify())
t=bsHomePage.select('#module\:_3_1 li a')
#print(t)
if not (os.path.exists(des)):
    os.mkdir(des)
for i in t:
    print(i)
    course_name=i.string[i.string.index(":")+1:].strip()
    #print(i.get('href'))
    if not (os.path.exists(os.path.join(des,course_name))):
        os.mkdir(os.path.join(des,course_name))
    if not (os.path.exists(os.path.join(des, course_name,"ppt"))):
        os.mkdir(os.path.join(des, course_name,"ppt"))
    current_path=os.path.join(des, course_name,"ppt")
    rcourse = sBB.get(host + i.get('href').strip(), headers=headers, verify=False)
    bsCourse = bs4.BeautifulSoup(rcourse.text, features="lxml")
    t = bsCourse.select('.navPaletteContent li a')
    rsourcepage = None
    for j in t:
        if j.span.string == '课程资源':
            rsourcepage = sBB.get(host + j.get('href').strip(), headers=headers, verify=False)
            break
    if (rsourcepage):
        download(current_path,rsourcepage,sBB)
print("BBhelper Update success")
