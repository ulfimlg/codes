import bs4 as bs
import requests

sauce = requests.get('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(sauce,'html.parser')

print()
