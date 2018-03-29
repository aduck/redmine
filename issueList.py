import requests
from bs4 import BeautifulSoup
from config import URL,COOKIE
# 获取列表
def getLists():
    lists = []
    headers = {'Cookie': COOKIE}
    r = requests.get(URL, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    # 需要的内容
    text = soup.find('table', class_ = 'issues').select('tbody tr.issue')
    # 需要的信息（issueId, issueName, issueStatus）
    for item in text:
        issueId = item.find('input')['value']
        issueName = item.select('.subject a')[0].get_text()
        issueStatus = item.select('.status')[0].get_text()
        lists.append({'issueId': issueId, 'issueName': issueName, 'issueStatus': issueStatus})
    return lists