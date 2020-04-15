import  requests
import  bs4
import os
from config import des,headers,host,ban_list
first_line=False
count=0
def set_first_line(x):
    global first_line
    first_line=x
def download(path, r, session):
        for i in ban_list:
            if os.path.normcase(path)==os.path.normcase(os.path.join(des,i)):
                return
        bsResource = bs4.BeautifulSoup(r.text, features="lxml")
        downloadlist_raw = bsResource.select('#content_listContainer a')
        downloadlist=[]
        #print(downloadlist)
        for i in downloadlist_raw:
            if not ('#' in i.get('href')):
                downloadlist.append(i)
        for i in downloadlist:
            flag=True
            rfile = session.head(host + i.get('href').strip(), headers=headers, verify=False,allow_redirects=True)
            if (i.span):
                span_name=i.span.string.strip()
            else:
                #print(i)
                span_name=i.contents[1].replace('\xa0',"")
                #print(span_name)
                flag=False
            if r'text/html' in rfile.headers['Content-Type']:
                if not os.path.exists(os.path.join(path,span_name)):
                    os.mkdir(os.path.join(path,span_name))
                rfile = session.get(host + i.get('href').strip(), headers=headers, verify=False)
                download(os.path.join(path,span_name), rfile, session)
            else:
                ExtendName = rfile.url[rfile.url.rfind('.'):]
                if flag:
                    full_name=os.path.join(path,span_name+ExtendName)
                else:
                    full_name = os.path.join(path, span_name)
                #print(full_name)
                if not os.path.exists(full_name):
                    rfile = session.get(host + i.get('href').strip(), headers=headers, verify=False)
                    with open(full_name,"wb") as f:
                        f.write(rfile.content)
                        if first_line:
                            print("")
                            set_first_line(False)
                        global count
                        count=count+1
                        print("create new file:     "+os.path.join(path,span_name+ExtendName))

