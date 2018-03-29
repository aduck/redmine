from issueList import getLists
from issueDtl import getDtl
from config import DATE
import time
from md import create
# 格式化日期
def formatDate(str):
    return time.mktime(time.strptime(str, '%Y-%m-%d'))
if __name__ == '__main__':
    lists = getLists() # 获取列表
    doneLists = [] # 已完成的列表
    doLists = [] # 进行中的列表
    todoLists = [] # 未开始的列表
    for item in lists:
        issueId = item['issueId']
        date = getDtl(issueId)
        # 开始日期
        startDate = date[0] or '1990-01-01'
        # 结束日期
        endDate = date[1] or '2099-12-31'
        item['startDate'] = startDate
        item['endDate'] = endDate
        # 已完成的issues
        if (formatDate(endDate) <= formatDate(DATE[1]) and formatDate(endDate) >= formatDate(DATE[0])) or (item['issueStatus'] in ['提测', '测试中', 'merge完成', '已关闭'] and formatDate(endDate) >= formatDate(DATE[0])):
            doneLists.append(item)
        # 未开始的列表
        elif formatDate(startDate) > formatDate(DATE[1]):
            todoLists.append(item)
        # 进行中的列表
        elif formatDate(endDate) > formatDate(DATE[1]):
            doLists.append(item)
    create(doneLists = doneLists, doLists = doLists, todoLists = todoLists)