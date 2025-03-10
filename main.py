from bs4 import BeautifulSoup


with open('website.html') as website:
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')
a_tags = soup.find_all('a')

h1 = soup.find(name='h1',id='name')
print(h1)

h3 = soup.find(name='h3', class_='heading')
print(h3)

for a in a_tags:
    # print(a.getText())
    print(a.attrs['href'])