from issueList import getLists
from issueDtl import getDtl
from config import DATE
import time
from html2 import create
# 格式化日期
def formatDate(str):
    return time.mktime(time.strptime(str, '%Y-%m-%d'))
if __name__ == '__main__':
    lists = getLists() # 获取列表
    curTasks = [] # 本周任务
    nextTasks = [] # 下周任务
    print('开始请求数据')
    for item in lists:
        issueId = item['issueId']
        dtl = getDtl(issueId)
        # 开始日期
        startDate = dtl['startDate'] or '1990-01-01'
        # 结束日期
        endDate = dtl['endDate'] or '1990-01-01'
        item['startDate'] = startDate
        item['endDate'] = endDate
        item['progress'] = dtl['progress']
        # 下周任务 task结束日期 > 本周末
        if formatDate(endDate) > formatDate(DATE[1]):
            # 去除已关闭功能
            if item['issueStatus'] != '已关闭':
                nextTasks.insert(0, item)
        # 本周任务 task结束日期 >= 本周初
        elif formatDate(endDate) > formatDate(DATE[0]):
            curTasks.insert(0, item)
    print('数据获取完成开始写入')
    create(curTasks = curTasks, nextTasks = nextTasks)