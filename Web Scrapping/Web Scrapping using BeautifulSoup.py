import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
import dateutil
r = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
assert result.status_code==200 
src = result.content
document = BeautifulSoup(src, 'lxml')
table = document.find("table")
print(table)
assert table.find("th").get_text() == "Rank"
df = pd.read_html(str(table))
df1 = pd.DataFrame(df[0])
print (df1)