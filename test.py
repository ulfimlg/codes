
#df = pd.read_csv('it.csv')
#df = df[['Sr no','Name','MoneyControl_link','News_link']]
link='http://www.moneycontrol.com/company-article/andhrabank/news/AB14#AB14'
#print(df['News_link'])
#with open('it.csv', newline='') as File:
#    reader = csv.reader(File)
#    for row in reader:
#        print(row)


import pandas as pd
csv_input = pd.read_csv('itt.csv')
p=csv_input['Name']
for x in p:
    y=[x for w in x if w not in [t for t in '%abcdefghijklmnopqrstuvwxyz+ABCDEFGHIJKLMNOPQRSTUVWXYZ.1234567890-/()']]
    print(y)
#csv_input['MoneyControl_link'] = p
#name=csv_input['Name']
#csv_input.to_csv('test.csv', index=False)
