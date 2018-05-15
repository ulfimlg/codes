# Import libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


headers = {
    'User-Agent': 'Nazim Girach',
    'From': 'nazimgirach@gmail.com'
}
page = requests.get('http://www.moneycontrol.com/news/business/cppib-allianz-to-acquire-55unitslt-sponsored-trust_10880121.html')
#page = requests.get('https://www.moneycontrol.com/news/business/prataap-snacks-looks-expensive-as-it-already-discounted-growth-story-akash-jain-2550553.html')
#page = requests.get('http://www.moneycontrol.com/news/business/scam-hit-pnb-refused-cvc39s-advice-against-its-corrupt-staff_10765161.html')
#create a bs4 object
soup = BeautifulSoup(page.text, 'html.parser')
x=soup.findAll('p')
#print(x)
length=len(x)
'''
for label in soup.select('p'):
    print(label.string)
    print("hello")

article = soup.find('article',class_='article_box')
print(article)
texts = article.find('div',class_='art-flow',id_='article-main')
print(texts)

extract_text = soup.find('p')
final_text = extract_text.get_text()
print(final_text)
'''
o=""
for i,j in enumerate(x):
    if(i<=(length-5)):
        op=j.getText()
        o=o+op


sid = SentimentIntensityAnalyzer()
print(o)
ss = sid.polarity_scores(o)
for k in ss:
    print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
