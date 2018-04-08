import requests
from bs4 import BeautifulSoup
from config import COOKIE
# 获取issue详情
def getDtl(id):
    url = 'http://pm.benlai.net/redmine/issues/%s' % id
    headers = {'Cookie': COOKIE}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    # 需要的内容(startDate, endDate, progress)
    startDate = soup.select('td.start-date')[0].get_text()
    endDate = soup.select('td.due-date')[0].get_text()
    progress = soup.select('p.percent')[0].get_text()
    return {
        'startDate': startDate,
        'endDate': endDate,
        'progress': float(progress.split('%')[0])
    }