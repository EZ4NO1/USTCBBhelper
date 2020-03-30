import requests
from config import  headers,url,url2,data
requests.packages.urllib3.disable_warnings()
def login():
    sLogin=requests.Session()
    r=sLogin.post(url, data=data, headers=headers, allow_redirects=False, verify=False)
    #print(r.headers['location'])
    sBB = requests.Session()
    r2=sBB.get(r.headers['location'], headers=headers, verify=False)
    r3=sBB.get('https://www.bb.ustc.edu.cn/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_2_1', headers=headers, verify=False);
    #print(r3.text)
    r4=sLogin.get(url2, headers=headers, allow_redirects=False, verify=False)
    #print(r4.status_code)
    r5=sBB.get(r4.headers['location'], headers=headers, verify=False)
    return sBB,r5