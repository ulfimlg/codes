import pandas as pd
csv_input = pd.read_csv('loll.csv')
x=content=csv_input['moneycontrol_link'][0:200]
p=[z for z in x]
pop=[]
for link in p:
    print(link)
    o=[pos for pos, char in enumerate(link) if char == '/']
    name=link[o[len(o)-1]+1:]
    print(name)
    lii=link[o[len(o)-2]+1:o[len(o)-1]]
    print(lii)
    news="http://www.moneycontrol.com/company-article/"+lii+"/news/"+name+"#"+name
    pop.append(news)
print(pop)
csv_input['news'][0:200]=pop
csv_input.to_csv('loll.csv', index=False)
