import requests, numpy as np
import lxml, html5lib
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
r1 = requests.get(url)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html5lib')
#<h3 class="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text">...</h3>
coverpage_news = soup1.find_all(class_='gs-c-promo-heading')

# Scraping the first 5 articles
number_of_articles = 15
# Empty lists for content, links and titles
list_links = []
list_titles = []
final_article = ''

for n in np.arange(0, number_of_articles):
    # Getting the link of the article
    link = 'https://www.bbc.com/'+coverpage_news[n]['href']
    if link not in list_links:
        list_links.append(link)
    else:
        continue

    # Getting the title
    title = coverpage_news[n].find('h3').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    print(str(n)+'. '+link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', property="articleBody")
    for p in body:
        paragraph = p.find_all('p')

    for p in paragraph:
        final_article = final_article +'\n'+ p.get_text()

print(final_article)
