'''
模拟美丽说登录
Created on 2014-12-26

@author: 2013159
'''
import urllib.request,http.cookiejar

def printDelimer():
    print("-"*30)

def readUrl(url):
    resp = urllib.request.urlopen(url)
    html = resp.read()
    return html.decode("utf-8")if __name__=='__main__':
    uname="XXXXXXX"
    pwd="XXXXXXXXX"
    url="https://account.meilishuo.com/user/login"
    print("meilishuo login begin")
    print("login url:"+url)
    printDelimer();
    
    cj = http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0')]
    
    #1、读取登陆页源码
    resp = opener.open(url)
    html = resp.read().decode("utf-8")
    printDelimer()
    #2、截取出nt 比较丑陋
    start = html.index("nt : '")+len("nt : '")
    nt=html[start:]
    end=nt.index("',")
    nt=nt[:end]
    print('--nt:'+nt+"----")
    
    
    loginMainUrl="https://account.meilishuo.com/aw/user/logon"
    
    postDict={
              'login_name':uname,
              'password':pwd,
              'save_state':'1',
              'check_code':'',
              'nt':nt
              }
    postData = urllib.parse.urlencode(postDict)
    postData = postData.encode('utf_8')
    resp2=opener.open(loginMainUrl,data=postData)
    for  c in cj:
        print(c.name,"="*6,c.value)
    
    personalUrl = 'https://account.meilishuo.com/settings/setPersonal'
    resp3=opener.open(personalUrl)
    
    print(resp3.read().decode("utf-8"))



