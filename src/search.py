# -*- coding:utf-8 -*-
import json,sys,os
from workflow import Workflow
import web
import requests

def main(wf):
    baseUrl = os.getenv('baseUrl')
    url = baseUrl + 'user?keyword=' 
    try:
        userList = requests.get(url).json()
        if len(userList) > 0:
            for item in userList:
                title = item['title']
                subtitle = item['subTitle']
                icon = item['icon']
                userId = item['userId']
                copyText = item['copyText']
                qlurl = item['url']
                if 'unReadCount' in item:
                    unReadCount = item['unReadCount']
                    if unReadCount > 0:
                     title = title + '      (🔴: ' + str(unReadCount) + ')'
                wf.add_item(title=title, subtitle=subtitle, icon=icon, largetext=title, copytext=copyText, quicklookurl=qlurl, arg=userId, valid=True)
        else:
            wf.add_item(title='找不到联系人…',subtitle='请重新输入')
    except IOError:
        wf.add_item(title='请先启动微信 & 登录…',subtitle='并确保安装微信小助手')
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
