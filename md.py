import time
from config import DATE
# 格式化日期
def formatDate(str):
    return time.mktime(time.strptime(str, '%Y-%m-%d'))
# 生成文档
def create(doneLists = [], doLists = [], todoLists = []):
    doneLen = len(doneLists)
    str = '### 本周工作内容\r'
    str += '|   | 工作内容 | 工作进度 | 开始时间 | 计划完成时间 | 备注 |\r'
    str += '| :-: | - | :-: | :-: | :-: | - |\r'
    # 已完成
    for index, doneItem in enumerate(doneLists):
        str += '| %s | %s | 100 | %s | %s | %s |\r' %((index + 1), doneItem['issueName'], doneItem['startDate'] if doneItem['startDate'] != '1990-01-01' else '', doneItem['endDate'] if doneItem['endDate'] != '2099-12-31' else '', doneItem['issueStatus'])
    # 进行中
    for index, doItem in enumerate(doLists):
        # 算百分比（一般情况需要减去两天周末）
        per = (formatDate(DATE[1]) + 86400.0 - formatDate(doItem['startDate'])) / (formatDate(doItem['endDate']) - formatDate(doItem['startDate']) - 86400.0 * 2) * 100
        # 备注
        note = per > 50 and '前端页面完成需要和api联调' or '前端功能待优化和与api联调'
        str += '| %s | %s | %d | %s | %s | %s |\r' %((index + 1 + doneLen), doItem['issueName'], per, doItem['startDate'] if doItem['startDate'] != '1990-01-01' else '', doItem['endDate'] if doItem['endDate'] != '2099-12-31' else '', note)
    # 未开始
    str += '\r\n'
    str += '### 下周工作计划\r'
    str += '|   | 工作内容 | 工作进度 | 开始时间 | 计划完成时间 | 备注 |\r'
    str += '| :-: | - | :-: | :-: | :-: | - |\r'
    for index, todoItem in enumerate(todoLists):
        str += '| %s | %s |  | %s | %s | \000 |\r' %((index + 1), todoItem['issueName'], todoItem['startDate'] if todoItem['startDate'] != '1990-01-01' else '', todoItem['endDate'] if todoItem['endDate'] != '2099-12-31' else '')
    str += '\r\n'
    with open('任务.md', 'w', encoding = 'utf-8') as f:
        f.write(str)
        print('写入完成')