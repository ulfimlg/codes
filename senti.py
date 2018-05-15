from textblob import TextBlob
senti="Edelweiss' research report on SymphonyPost a bleak Q1, Symphony (SYML) registered strong recovery in Q2/Q3FY18, with 20% plus YoY revenue growth driving all-time peak off-season margins for it. Key highlights: a) strong re-stocking ahead of summer season helped SYML clock 18/21% QoQ/YoY growth in revenue, implying 10% YoY growth for 9mFY18; b) SYML has received strong response for its six new SKUs under diamond & silver range, which translated into better realisations and profitability (gross/EBIDTA margins up by 70/260bps to 54.3%/39.9%); c) with market share in organised coolers peaking at 50-55%, management is banking on growth in the organised basket led by shift, early signs of which are already visible.OutlookSYML’s earnings growth visibility stays strong owing to dismal ~12% penetration for air coolers and huge scope for organised players to gain ground. Despite rising competition, we believe SYML will retain its positioning leaving little room for disappointment. Downgr"
senti=senti+"ade to ‘HOLD/SP’ from ‘BUY/SO’.For all recommendations report, click hereDisclaimer: The views and investment tips expressed by investment experts/broking houses/rating agencies on moneycontrol.com are their own, and not that of the website or its management. Moneycontrol.com advises users to check with certified experts before taking any investment decisions."
t = TextBlob(senti)
tp=t.sentiment.polarity
print(senti)
print(tp)
t = TextBlob("This is awesome!!")
tp=t.sentiment.polarity
print("This is awesome!!")
print(tp)
t = TextBlob("Aircel to file for bankruptcy")
tp=t.sentiment.polarity
print("Aircel to file for bankruptcy")
print(tp)
t = TextBlob("I am sad")
tp=t.sentiment.polarity
print("I am sad")
print(tp)
