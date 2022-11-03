import argparse
from poc import poc
# 艺术字模块
from pyfiglet import Figlet
print('=='*70)
print('I hope all network security enthusiasts have good luck')
# 定义艺术字
f = Figlet(font="slant",width=100)
print(f.renderText('cve-2021-41773'))
print('小白poc&exp练手项目。 声明：该项目来自作者日常学习笔记。 请勿利用相关技术以及工具从事非法测试，如因此产生的一切不良后果作者无关。')
print('=='*70)
# def base_url(url):
#     if url.endswith('/') == True:
#         request = re.sub('/\\n','',url)
#     else :
#         request = re.sub('\\n','',url)

# 1. 定义命令行解析器对象
parser = argparse.ArgumentParser(description='Demo of argparse')
 
# 2. 添加命令行参数
parser.add_argument('-u', '--url',help='`Please enter http(s)://ip:port`')
# parser.add_argument('--batch', type=int, default=4)
 
# 3. 从命令行中结构化解析参数
args = parser.parse_args()
url = args.url
# print("url:",args.url)
if poc(url):
    print('Good Luck')
    # exp(url)
else:
    print("g")