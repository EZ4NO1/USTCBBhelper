import  requests
import  bs4
from login import login
import os
from config import des,headers,host
from download import  download,set_first_line
from os import path

if __name__=="__main__":
    requests.packages.urllib3.disable_warnings()
    sBB,rHomePage=login()
    bsHomePage=bs4.BeautifulSoup(rHomePage.text,features="lxml")
    #print(bsHomePage.prettify())
    t=bsHomePage.select('#module\:_3_1 li a')
    #print(t)
    if not (os.path.exists(des)):
        os.mkdir(des)
    for k,i in zip(range(len(t)),t):
        set_first_line(True)
        if i.string.find(":")==-1:
            continue
        course_name=i.string[i.string.index(":")+1:].strip()
        print("\rBBhelper:["+str(k+1)+"/"+str(len(t))+"] Updating Course "+course_name,end="")
        #print(i.get('href'))
        if not (os.path.exists(os.path.join(des,course_name))):
            os.mkdir(os.path.join(des,course_name))
        if not (os.path.exists(os.path.join(des, course_name,"ppt"))):
            os.mkdir(os.path.join(des, course_name,"ppt"))
        current_path=os.path.join(des, course_name,"ppt")
        rcourse = sBB.get(host + i.get('href').strip(), headers=headers, verify=False)
        bsCourse = bs4.BeautifulSoup(rcourse.text, features="lxml")
        tt = bsCourse.select('.navPaletteContent li a')
        rsourcepage = None
        for j in tt:
            if j.span.string == '课程资源':
                rsourcepage = sBB.get(host + j.get('href').strip(), headers=headers, verify=False)
                break
        if (rsourcepage):
            download(current_path,rsourcepage,sBB)
    from download import count
    if (count==0):
        print("\nBBhelper: your files have already benn newest")
    else:
        print("\nBBhelper: "+str(count)+" files have benn created")