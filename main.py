from bs4 import BeautifulSoup
import requests

URL = 'https://appbrewery.github.io/news.ycombinator.com/'

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
first_article = soup.find(name='a', class_='storylink').getText()
article_link = soup.find(name='a', class_='storylink').get('href')
article_upvote = soup.find(name='span', id='score_40725924').getText()
print(article_upvote)















#
# with open('website.html') as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# a_tags = soup.find_all('a')
#
# h1 = soup.find(name='h1',id='name')
# print(h1)
#
# h3 = soup.find(name='h3', class_='heading')
# print(h3)
#
# for a in a_tags:
#     # print(a.getText())
#     print(a.attrs['href'])
#
# company_url = soup.select_one(selector='p a')
# print(company_url)