import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

a="Great place to be when you are in Bangalore."
b="The place was being renovated when I visited so the seating was limited."
c="Loved the ambience, loved the food"
d="The food is delicious but not over the top."
e="Service - Little slow, probably because too many people."
f="The place is not easy to locate"
g="Mushroom fried rice was tasty"

hotel_rev = [a,b,c,d,e,f,g]

sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()
