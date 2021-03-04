# -*- coding=utf-8 -*-
# 提取答案的方法

"""
直接调用下列的方法，无需带入参数即可

"""


"""
用'正则提取式'从接口返回的内容中提取'单选题'答案
"""


def getChoiceAns():
    import re

    with open('info.json') as f:  # 打开文件准备读取
        ans = f.read()  # 读取文件内的内容赋值给变量
        # print(ans)
        # print(type(ans))
    y = re.findall(r'answer":"(.+?)","', ans)  # 正则提取表达式，非贪婪匹配，提取answer的value | 方法来源：https://blog.csdn.net/bang152101/article/details/89284249
    # print(y)
    # print(type(y))
    l = ''.join(y)  # 将正则提取出的列表中的内容以字符串的方式提取出来 | 方法来源：https://www.py.cn/faq/python/17322.html
    # print(l)
    return l


"""
用正则提取后放入数组，得到一个填空题答案的数组
"""


def getFillAns():
    import re
    import json

    with open('info.json', 'r') as f:
        ans = f.read()

    y = re.findall("b'(.+?)'", ans)     # 正则提取去除接口返回内的b''
    for i in y:
        y = re.findall('"answer":(.+?),"c', ans)    # 正则提取回参中的answer后的部分
        # print(y)

    ll = []
    for i in y:
        u = i.split("],[")      # 正则提取多个填空中的答案
        # print(u)
        for j in u:
            # print('准备提取')
            y = re.findall(r'content":"(.+?)"', j)      # 正则提取答案的主体内容
            # print('提取成功')
            for t0 in y:
                t1 = t0.encode().decode('unicode_escape')   # 两次encode后decode解决反斜杠的问题
                t = t1.encode().decode('unicode_escape')
                # print(t)
                # print(type(t))
                ll.append(t)    # 存入最终要传给前端的列表
                # print(ll)
                break
    # print(ll)
    return ll  # 返回的为一个数组，具体放在指令中的执行方法看底部执行方式


def getMultiChoice():
    import re

    with open('info.json') as f:  # 打开文件准备读取
        ans = f.read()  # 读取文件内的内容赋值给变量
        # print(ans)
        # print(type(ans))
    y = re.findall(r'answer":"(.+?)","', ans)  # 正则提取表达式，非贪婪匹配，提取answer的value | 方法来源：https://blog.csdn.net/bang152101/article/details/89284249
    # print(y)
    # print(type(y))
    l = ''.join(y)  # 将正则提取出的列表中的内容以字符串的方式提取出来 | 方法来源：https://www.py.cn/faq/python/17322.html
    # print(l)
    ll = list(l)
    return ll


if __name__ == '__main__':
    # tt = getFillAns()
    # print('tt=%s' % tt)
    # driver.execute_script(r"window.initFillAnswer(%s)" % tt)
    ll =getFillAns()
    print(ll)

