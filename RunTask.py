# -div- coding=utf-8 -div-
# mitmproxy结合selenium AMT测试全流程

# 导入库
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scriptGetans import getChoiceAns, getFillAns, getMultiChoice
import time
import json
import os
import platform

platform_type = platform.system()       # 获取当前系统类型名称
if platform_type == 'Windows':      # 根据系统判断执行哪个chromedriver
    # 进行chrome的设置
    chrome_path = './chromedriver.exe'  # 设置chromedriver路径
else:
    chrome_path = './chromedriver'

with open('deviceName.txt', 'r') as f:      # 从配置文件读取手机型号并赋值给一个变量
    mobileType = f.read()
# mobileEmulation = {'deviceName': 'iPhone 8 Plus'}  # 设置固定的手机型号
mobileEmulation = {'deviceName': mobileType}    # 手机型号参数复制给浏览器设置参数
# mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}  # 设置分辨率
chrome_options = Options()  # 创建chrome设置
chrome_options.add_argument('--proxy-server=127.0.0.1:1010')  # 增加监听mitm代理端口的设置
chrome_options.add_argument('--ignore-certificate-errors')  # 无视证书引发的错误
chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)  # 增加模拟手机的设置
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)  # 配置chrome设置
# 通过输入确认值开启mitmproxy的方法
print('请手动开启mitmproxy代理:')
print('确认是否已运行mitm? 输入(yes/y)或(no/n)')
whether_open = input()  # 手动确认是否已经启动了代理
if whether_open == 'y' or whether_open == 'yes':    # 判断手动输入的值是否对应已开启代理

    print('mitmproxy已启动，正在启动bmp代理')

    # # 用shell开启mitmproxy代理
    # os.chdir('./')  # 将路径设置到当前project地址
    # os.system('mitmweb -s mitmproxy\ addon.py -p 1010')  # shell中运行mitmproxy

    print('请输入作业类型，仅支持输入AT/AMT/MT，不区分大小写')
    print('作业类型：')
    hw_type = input()
    # welcome_url = "http://dinghw.test.51x-study.com/self/welcome?jupiterToken=eyJjb3JwSWQiOiJkaW5nYjdhMDc2ZmZjNDczZWRkMDI0ZjJmNWNjNmFiZWNiODUiLCJzdWJtaXRvcklkIjoiNzczMjYzMjgwMzY1OTAxNCIsImFjY291bnRJZCI6NzczMjYzMjgwMzY3ODY5MCwidXNlcklkIjo2NjMyNjMyODAzNjkwNjUyLCJkZFN0dWRlbnRJZCI6IjE1OTY0NDM1Mjk0ODMtNjUyMTU3NTAwIiwicmVhbE5hbWUiOiJcdTY3OTdcdTRlYzFcdTY3NzBcdTU5MjdcdTU0ZTUiLCJyb2xlIjoxLCJjbGFzc0lkIjozNDIxNjAxMjksImNsYXNzTmFtZSI6IjIwMTdcdTVlNzRcdTdlYTcxXHU3M2VkKFx1NWJiNlx1NjgyMVx1NmQ0Ylx1OGJkNVx1N2ZhNCkiLCJkZFRlYWNoZXJJZCI6IjE1OTE0NjE5OTk5NzMiLCJod0lkIjoxMDI4Mzk5NjQ3MSwiaHdUeXBlIjoyLCJod05hbWUiOiI5XHU2NzA4OVx1NjVlNVx1NjU3MFx1NWI2NiIsImh3VGltZSI6MTU5OTYyMDIxMiwic3ViamVjdElkIjoyLCJzdWJqZWN0TmFtZSI6Ilx1NjU3MFx1NWI2NiIsImNvdXJzZUlkIjoxMDI1MTk5MDEyNDc0NDQ4LCJjb3Vyc2VOYW1lIjoiMjAxOVx1NzljYlx1NWI2M1x1NTIxZFx1NGUyZFx1NjU3MFx1NWI2Nlx1NmNhYVx1NjU1OVx1NzI0OFx1NGU1ZFx1NWU3NFx1N2VhN1x1NmI2M1x1NWYwZlx1OGJmZSIsInN0YWdlIjo0MCwiYnZDb2RlIjoyNSwiYnZOYW1lIjoiXHU2Y2FhXHU2NTU5XHU3MjQ4IiwiZXN0aW1hdGVUaW1lIjoiMTI5MCIsInRhZ0NvZGVDbnQiOjAsInF1ZXN0aW9uQ250IjowfQO0O0OO0O0O"

    # 通过配置文件读取带有token的链接
    print('正在打开链接...')
    with open('url.txt', 'r') as f:
        welcome_url = f.read()

    # 通过shell窗口输入带有token的链接的方式
    # print('请输入带有token的链接，如果链接输入错误，程序可能会报错！')
    # print('url:')
    # welcome_url = input()   # 手动输入带有token的链接
    # print('链接已输入，正在浏览器内跳转页面')

    driver.get(welcome_url)  # 打开链接
    time.sleep(2)  # 静置时间

    if hw_type == 'at' or hw_type == 'AT':
        driver.find_element_by_xpath("//div[@id='cont-card']/div[3]/button").click()  # 点击进入作业AT
    else:
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[1]/div[2]/div[2]/button").click()   # 点击进入作业MT/AMT
    print('已进入做题流程，请等待自动刷新后开始做题')
    time.sleep(2)  # 静止时间
    # question_url = "https://app46795.eapps.dingtalkcloud.com/self/question"
    # driver.get(question_url)
    driver.refresh()    # 刷新页面
    print('页面刷新结束')


    # 以下为获取go接口的内容，取答案，做题
    check_if = True

    if hw_type == 'MT' or hw_type == 'mt':
        # MT做题流程的总循环
        while check_if:
            print('正在获取当前题型名称...')
            time.sleep(1)

            title = driver.find_element_by_xpath("//div[@id='question-content']/div/div[1]/div[1]/h1/span[2]")    # 获取题型名称开始做题
            judge_title = title.text
            print('当前题目题型:', judge_title)

            # 根据标题名称，选择做题流程
            if judge_title == '单选题':

                """
                单选题做题流程部分
                """
                print('选择题答题中...')
                time.sleep(1)
                ans = getChoiceAns()
                print('本题答案：', ans)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                if ans == 'A':
                    try:
                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div").click()
                    except Exception as e:
                        print('脚本速度过快，未能找到按钮！')
                elif ans == 'B':
                    try:
                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                    except Exception as e:
                        print('脚本速度过快，未能找到按钮！')
                elif ans == 'C':
                    try:
                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                    except Exception as e:
                        print('脚本速度过快，未能找到按钮！')
                elif ans == 'D':
                    try:
                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                    except Exception as e:
                        print('脚本速度过快，未能找到按钮！')
                else:
                    print('本题未能取到答案！')
                try:
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button[2]").click()
                    check_if = True

                except Exception as e:
                    check_if = False
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button[3]").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div[3]/button").click()    # 点击答题卡提交按钮
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[3]/button[2]").click()   # 点击提交确认框的提交按钮
                    print('做题流程结束')

            elif judge_title == '填空题':

                """
                填空题做题部分流程
                """
                print('填空题答题中...')
                time.sleep(1)
                ans = getFillAns()
                print('填空题答案暂时不展示，请查看浏览器页面')
                driver.execute_script(r"window.initFillAnswer(%s)" % ans)
                try:
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button[2]").click()
                    check_if = True

                except Exception as e:
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button[3]").click()
                    check_if =False
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div[3]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[3]/button[2]").click()
                    print('做题流程结束')

            elif judge_title == '多选题':

                """
                多选题做题部分流程
                """
                print('多选题答题中...')
                time.sleep(1)
                ans = getMultiChoice()
                print('本题答案：', ans)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                # 拿到一个题目的答案的list，去遍历进行点击操作
                for s_choice in ans:
                    if s_choice == 'A':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[1]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif s_choice == 'B':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif s_choice == 'C':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif s_choice == 'D':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    else:
                        print('本题未能找到答案')

                # 题目的选项选好了，点击提交进入下一题
                try:
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button[2]").click()
                    check_if = True
                except Exception as e:
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button[3]").click()
                    check_if = False
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div[3]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[3]/button[2]").click()
                    print('做题流程结束')

            else:
                print('没有找到题目类型，脚本结束')
                break

    elif hw_type == 'AMT' or hw_type == 'amt':
        # AMT做题流程的总循环
        while check_if:
            # driver.refresh()
            print('正在获取当前题型名称...')
            time.sleep(2)
            try:
                title = driver.find_element_by_xpath("//div[@id='question-content']/div[1]/div[1]/div[1]/div[1]/h1/span[2]")    # 获取题型名称开始做题
                judge_title = title.text
                print('当前题目题型:', judge_title)

                if judge_title == '单选题':

                    print('选择题答题中...')
                    time.sleep(1)
                    ans = getChoiceAns()
                    print('本题答案：', ans)
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                    if ans == 'A':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif ans == 'B':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif ans == 'C':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif ans == 'D':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    else:
                        print('本题未能取到答案！')

                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                elif judge_title == '填空题':

                    print('填空题答题中...')
                    time.sleep(1)
                    ans = getFillAns()
                    print('填空题答案暂时不展示，请查看浏览器页面')
                    driver.execute_script(r"window.initFillAnswer(%s)" % ans)

                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                elif judge_title == '多选题':

                    print('多选题答题中...')
                    time.sleep(1)
                    ans = getMultiChoice()
                    print('本题答案：', ans)
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                    # 拿到一个题目的答案的list，去遍历进行点击操作
                    for s_choice in ans:
                        if s_choice == 'A':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[1]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        elif s_choice == 'B':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        elif s_choice == 'C':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        elif s_choice == 'D':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        else:
                            print('本题未能找到答案')

                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                else:
                    print('没有找到题目类型，脚本结束')

                check_if = True

            except Exception as e:
                check_if = False
                try:
                    time.sleep(2)
                    driver.find_element_by_xpath("//div[@id='app']/div/div/footer/button[2]").click()
                    print('做题流程结束')
                except Exception as e:
                    print('没有找到题目类型，脚本结束')

    elif hw_type == 'AT' or hw_type == 'at':
        # AT做题流程的总循环
        check_if_test = True
        print('正在等待页面加载...')
        time.sleep(5)   # 等待题目生成
        while check_if_test:
            # time.sleep(5)
            driver.refresh()    # 刷新页面确保接口返回内容保存值正确
            print('正在获取当前题型名称...')
            time.sleep(2)   # 等待页面加载完成
            try:
                title = driver.find_element_by_xpath("//div[@id='question-content']/div[1]/div[1]/div[1]/div[1]/h1/span[2]")    # 获取题型名称开始做题
                judge_title = title.text
                print('当前题目题型:', judge_title)

                if judge_title == '单选题':

                    print('选择题答题中...')
                    time.sleep(1)
                    ans = getChoiceAns()
                    print('本题答案：', ans)
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                    if ans == 'A':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif ans == 'B':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif ans == 'C':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    elif ans == 'D':
                        try:
                            driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                        except Exception as e:
                            print('脚本速度过快，未能找到按钮！')
                    else:
                        print('本题未能取到答案！')

                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button").click()

                elif judge_title == '填空题':

                    print('填空题答题中...')
                    time.sleep(1)
                    ans = getFillAns()
                    print('本题答案：', ans)
                    # print('填空题答案暂时不展示，请查看浏览器页面')
                    driver.execute_script(r"window.initFillAnswer(%s)" % ans)

                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button").click()

                elif judge_title == '多选题':

                    print('多选题答题中...')
                    time.sleep(1)
                    ans = getMultiChoice()
                    print('本题答案：', ans)
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                    # 拿到一个题目的答案的list，去遍历进行点击操作
                    for s_choice in ans:
                        if s_choice == 'A':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[1]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        elif s_choice == 'B':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        elif s_choice == 'C':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        elif s_choice == 'D':
                            try:
                                driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                            except Exception as e:
                                print('脚本速度过快，未能找到按钮！')
                        else:
                            print('本题未能找到答案')

                    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[2]/button").click()

                else:
                    print('没有找到题目类型，进入下一阶段')
                    break

                check_if_test = True

            except Exception as e:
                # check_if_test = False
                try:
                    print('正在等待页面加载...')
                    time.sleep(5)   # 等待生成测试结果
                    driver.find_element_by_xpath("//div[@id='app']/div/div/footer/button[2]").click()  # 提交测试答案
                    check_if_test = False
                except Exception as e:
                    print('没有找到题目类型，进入下一阶段')
                    break

        print('AT测试部分结束，接下来进入学习部分...')

        # AT先测完成，进入学习部分
        print('等待页面加载...')
        driver.refresh()
        # time.sleep(2)
        check_if_task = True
        time.sleep(5)
        while check_if_task:
            try:
                # 有多个知识点进行练习的，分为多个小的模块
                # time.sleep(5)
                driver.find_element_by_xpath("//div[@id='app']/div/footer/button").click()  # 点击开始练习按钮

                check_if_practise = True
                while check_if_practise:
                    driver.refresh()
                    print('正在获取当前题型名称...')
                    time.sleep(2)
                    try:
                        title = driver.find_element_by_xpath("//div[@id='question-content']/div[1]/div[1]/div[1]/div[1]/h1/span[2]")  # 获取题型名称开始做题
                        judge_title = title.text
                        print('当前题目题型:', judge_title)

                        if judge_title == '单选题':

                            print('选择题答题中...')
                            time.sleep(1)
                            ans = getChoiceAns()
                            print('本题答案：', ans)
                            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                            if ans == 'A':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            elif ans == 'B':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            elif ans == 'C':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            elif ans == 'D':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            else:
                                print('本题未能取到答案！')

                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                        elif judge_title == '填空题':

                            print('填空题答题中...')
                            time.sleep(1)
                            ans = getFillAns()
                            print('本题答案：', ans)
                            # print('填空题答案暂时不展示，请查看浏览器页面')
                            driver.execute_script(r"window.initFillAnswer(%s)" % ans)

                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                        elif judge_title == '多选题':

                            print('多选题答题中...')
                            time.sleep(1)
                            ans = getMultiChoice()
                            print('本题答案：', ans)
                            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                            # 拿到一个题目的答案的list，去遍历进行点击操作
                            for s_choice in ans:
                                if s_choice == 'A':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[1]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                elif s_choice == 'B':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                elif s_choice == 'C':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                elif s_choice == 'D':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                else:
                                    print('本题未能找到答案')

                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                        else:
                            print('没有找到题目类型，脚本结束')

                        check_if_practise = True

                    except Exception as e:
                        # check_if_practise = False
                        try:
                            time.sleep(2)
                            driver.find_element_by_xpath("//div[@id='app']/div/div/footer/button[2]").click()  # 交作业的按钮
                            check_if_task = False
                            check_if_practise = False
                        except Exception as e:
                            try:
                                time.sleep(2)
                                driver.find_element_by_xpath("//div[@id='app']/div/footer/button").click()  # 开始练习按钮
                                check_if_practise = True
                            except Exception as e:
                                print('没有找到题目类型，脚本结束')
                                break


            except Exception as e:
                # 只有单一知识点，一个模块的
                check_if_practise = True
                while check_if_practise:
                    print('正在获取当前题型名称...')
                    time.sleep(2)
                    try:
                        title = driver.find_element_by_xpath("//div[@id='question-content']/div[1]/div[1]/div[1]/div[1]/h1/span[2]")  # 获取题型名称开始做题
                        judge_title = title.text
                        print('当前题目题型:', judge_title)

                        if judge_title == '单选题':

                            print('选择题答题中...')
                            time.sleep(1)
                            ans = getChoiceAns()
                            print('本题答案：', ans)
                            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                            if ans == 'A':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            elif ans == 'B':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            elif ans == 'C':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            elif ans == 'D':
                                try:
                                    driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                                except Exception as e:
                                    print('脚本速度过快，未能找到按钮！')
                            else:
                                print('本题未能取到答案！')

                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                        elif judge_title == '填空题':

                            print('填空题答题中...')
                            time.sleep(1)
                            ans = getFillAns()
                            print('填空题答案暂时不展示，请查看浏览器页面')
                            driver.execute_script(r"window.initFillAnswer(%s)" % ans)

                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                        elif judge_title == '多选题':

                            print('多选题答题中...')
                            time.sleep(1)
                            ans = getMultiChoice()
                            print('本题答案：', ans)
                            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将页面拉到最底部，不然找不到选项

                            # 拿到一个题目的答案的list，去遍历进行点击操作
                            for s_choice in ans:
                                if s_choice == 'A':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[1]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                elif s_choice == 'B':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[2]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                elif s_choice == 'C':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[3]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                elif s_choice == 'D':
                                    try:
                                        driver.find_element_by_xpath("//div[@id='answers']/div/div/div[4]").click()
                                    except Exception as e:
                                        print('脚本速度过快，未能找到按钮！')
                                else:
                                    print('本题未能找到答案')

                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/ul/li[3]/button").click()

                        else:
                            print('没有找到题目类型，脚本结束')
                            break

                        check_if_practise = True

                    except Exception as e:
                        try:
                            time.sleep(2)
                            driver.find_element_by_xpath("//div[@id='app']/div/div/footer/button[2]").click()  # 交作业的按钮
                            check_if_practise = False
                            check_if_task = False
                        except Exception as e:
                            # print('没有找到题目类型，脚本结束')
                            check_if_practise = False
                            check_if_task = False

        print('检测到做题流程已结束')




else:
    print('未能打开mitmproxy，程序退出')

"""
出整体循环，做题至此结束
"""
print('请手动关闭退出本程序')