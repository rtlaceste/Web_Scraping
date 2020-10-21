import requests
from bs4 import BeautifulSoup as bs4
import pprint

res = requests.get('https://news.ycombinator.com/news') # url of website for scraping
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = bs4(res.text, 'html.parser') # To init html parser
soup2 = bs4(res2.text, 'html.parser')
links = soup.select('.storylink') #.(class) to select class name from html code
subtext = soup.select('.subtext') #selecting subtext class from html

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse=True) # sort list by 'votes' key in dictionary

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes':points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))