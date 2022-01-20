from bs4 import BeautifulSoup
import requests
#import xlrd
import pandas as pd

loc = ("/Users/pratikshaphadtare/Downloads/Input.xlsx")
data = pd.read_excel(loc)

#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
 
def getIdLink(x):
    index = int(x)
    URL_ID = int(data.iat[x,0])
    link = str(data.iat[x,1])

    return URL_ID, link

a,b = data.shape
rows = a-1

with open('read.txt', 'w') as file:
 for x in range(rows):
    id, link = getIdLink(x)

    html_text = requests.get(link, headers = headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    title = soup.find('h1', class_ = "entry-title").text
    articles = soup.find('div', class_="td-post-content").text
   
    file.writelines("% s" % data for data in articles)
    print(title)
    print(articles)

with open('read.txt','r') as f:
  stop_words = f.read()

stop_words = stop_words.split('\n')
print(f'Total number of Stop Words are {len(stop_words)}')

with open('read.txt', 'w') as file:
    articles = ['title/n','articles/n']
    file.writelines("% s\n" % data for data in articles)
