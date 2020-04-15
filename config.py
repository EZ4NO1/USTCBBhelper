headers = {
'Connection': 'keep-alive',
#'Content-Length': '328',
#'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36 Edg/83.0.461.1'
}
url=r"https://passport.ustc.edu.cn/login?service=http%3A%2F%2Fwww.bb.ustc.edu.cn%2Fnginx_auth%2Flogin.php%3Fnext%3D68747470733a2f2f7777772e62622e757374632e6564752e636e2f776562617070732f706f7274616c2f657865637574652f746162732f746162416374696f6e3f7461625f7461625f67726f75705f69643d5f315f31"
url2=r'https://passport.ustc.edu.cn/login?service=https%3a%2f%2fwww.bb.ustc.edu.cn%2fwebapps%2fbb-SSOIntegrationDemo-BBLEARN%2fexecute%2fauthValidate%2fcustomLogin%3freturnUrl%3dhttp%3a%2f%2fwww.bb.ustc.edu.cn%2fwebapps%2fportal%2fframeset.jsp%26authProviderId%3d_103_1'
data={
'model': 'uplogin.jsp',
'service': r'http://www.bb.ustc.edu.cn/nginx_auth/login.php?next=68747470733a2f2f7777772e62622e757374632e6564752e636e2f776562617070732f706f7274616c2f657865637574652f746162732f746162416374696f6e3f7461625f7461625f67726f75705f69643d5f315f31',
'warn': '',
'showCode':'',
'username': 'PB17030852',
'password': 'abc6123666',
'button': ''
}
host=r'https://www.bb.ustc.edu.cn'
des=r'D:\\BBhelper'
ban_list=[r'数据库系统及应用\ppt\demo'] #不下视频