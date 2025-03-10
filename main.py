from operator import index

from bs4 import BeautifulSoup
import requests

URL = 'https://appbrewery.github.io/news.ycombinator.com/'

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
first_article = soup.find_all(name='a', class_='storylink')
article_link = soup.find_all(name='a', class_='storylink')
article_upvote = soup.find_all(name='span', class_='score')

articles = [article.getText() for article in first_article]
article_links = [link.get('href') for link in article_link]
article_upvotes = [int(vote.getText().split()[0]) for vote in article_upvote]

highest_score = max(article_upvotes)
highest_score_index = article_upvotes.index(highest_score)

highest_score_article = {
    'article': articles[highest_score_index],
    'url': article_links[highest_score_index],
    'score': article_upvotes[highest_score_index]
}

for key, value in highest_score_article.items():
    print(f'{key}: {value}')

# a= 0
# for vote in article_upvotes:
#     if vote > a:
#         a = vote
#
# if a in article_upvotes:
#     index = article_upvotes.index(a)
# print(articles[index])
# print(article_links[index])

# collection = zip(articles,article_links,article_upvotes)
# for item in collection:
#     print(item)
















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