# -*- coding=utf-8 -*-
# mitmproxy启动配置文件
"""
shell或cmd运行mitmproxy时，建议使用mitmweb命令运行
运行指令为：
mitmweb --set http2=false -p 1010 -s MitmproxyAddon.py

--set https2=false 的意义为关闭http2的访问方式，以免出现code为413的加载不出资源的问题
-p 端口
-s 配置文件
"""

# 导入库
from mitmproxy import http


"""在request中添加新的body入参"""


def request(flow: http.HTTPFlow) -> None:
    if flow.request.urlencoded_form:
        # 如果原本已有表单，此操作仅会新增dict型数据
        flow.request.urlencoded_form["withans"] = "1941da"
    # 也可以单独传递新的表单，会覆盖原有的请求体
    # else:
    #     flow.request.urlencoded_form = [
    #         ("test", "test")
    #     ]


"""从/go里面取出response，并且保存到对应的文件中"""


def response(flow: http.HTTPFlow) -> None:
    print(flow.response.content)
    response_content = flow.response.content    # 将返回的参数都保存到一个变量
    if "questionInfo" in str(response_content):  # 查找接口返回内容将其中含有questionInfo字段的回参整个保存到文件中
        with open('/Users/athlonhd/QA-project-cl/info.json', 'w') as f:      # 此处文件路径必须为绝对路径，不然无法写入
            f.write(str(response_content))



"""添加请求头Token"""

"""
class AddHeader:
    def __init__(self):
        # 从txt中取token
        self.token = 

    def request(self, flow):
        # 将Token放于Headers中
        flow.request.headers["Token"] = str(self.token)


addons = [
    AddHeader()
]
"""