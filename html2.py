import time
from config import DATE
# 格式化日期
def formatDate(str):
    return time.mktime(time.strptime(str, '%Y-%m-%d'))
# 生成文档
def create(curTasks = [], nextTasks = []):
    str = '''
<table class="confluenceTable">
  <tbody>
    <tr>
      <th colspan="6" style="text-align: center;" class="confluenceTh">本周工作内容</th>
    </tr>
    <tr>
      <th class="confluenceTh">&nbsp;</th>
      <th class="confluenceTh">工作内容</th>
      <th class="confluenceTh">工作进度</th>
      <th colspan="1" class="confluenceTh">开始时间</th>
      <th class="confluenceTh">计划完成时间</th>
      <th class="confluenceTh">备注</th>
    </tr>
    '''
    # 本周工作内容
    for index, task in enumerate(curTasks):
        if task['issueStatus'] in ['提测', '测试中', '测试完成', 'merge完成', '已关闭']:
            per = 100
            note = task['issueStatus']
        else:
            per = task['progress'] if task['progress'] else 50
            note = '前端页面开发完成，需要与api联调' if per > 50 else '前端页面待完善优化以及与api联调'
        str += '''
    <tr>
      <td class="confluenceTd">%d</td>
      <td class="confluenceTd">
        <p>%s</p>
      </td>
      <td class="confluenceTd">%d%%</td>
      <td colspan="1" class="confluenceTd">%s</td>
      <td class="confluenceTd">%s</td>
      <td class="confluenceTd">%s</td>
    </tr>
        ''' %(index + 1, task['issueName'], per, task['startDate'], task['endDate'], note)
    # 下周工作计划
    str += '''
    <tr><th colspan="6" style="text-align: center;" class="confluenceTh">下周工作计划</th></tr>
    <tr>
      <th class="confluenceTh">&nbsp;</th>
      <th class="confluenceTh">工作内容</th>
      <th class="confluenceTh">工作进度</th>
      <th colspan="1" class="confluenceTh">开始时间</th>
      <th class="confluenceTh">计划完成时间</th>
      <th class="confluenceTh">备注</th>
    </tr>
    '''
    for index, task in enumerate(nextTasks):
        per = task['progress']
        if per > 50:
            note = '前端页面开发完成，需要与api联调'
        elif per == 0:
            note = ''
        else:
            note = '前端页面待完善优化以及与api联调'
        str += '''
    <tr>
      <td class="confluenceTd">%d</td>
      <td class="confluenceTd">
        <p>%s</p>
      </td>
      <td class="confluenceTd">%d%%</td>
      <td colspan="1" class="confluenceTd">%s</td>
      <td class="confluenceTd">%s</td>
      <td class="confluenceTd">%s</td>
    </tr> 
    ''' %(index + 1, task['issueName'], per, task['startDate'], task['endDate'], note)
    str += '''
    </tbody>
</table>
    '''
    with open('任务.html', 'w', encoding = 'utf-8') as f:
        f.write(str)
        print('写入完成')