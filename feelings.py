from textblob import TextBlob

a="Post a bleak Q1, Symphony (SYML) registered strong recovery in Q2/Q3FY18, with 20% plus YoY revenue growth driving all-time peak off-season margins for it. Key highlights: a) strong re-stocking ahead of summer season helped SYML clock 18/21% QoQ/YoY growth in revenue, implying 10% YoY growth for 9mFY18; b) SYML has received strong response for its six new SKUs under diamond & silver range, which translated into better realisations and profitability (gross/EBIDTA margins up by 70/260bps to 54.3%/39.9%); c) with market share in organised coolers peaking at 50-55%, management is banking on growth in the organised basket led by shift, early signs of which are already visible. "
b=TextBlob(a)
x=b.sentiment.polarity
print(x)
