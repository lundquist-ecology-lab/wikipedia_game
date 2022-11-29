
import pandas as pd
import requests
import wikipedia
import re
from bs4 import BeautifulSoup

query = ['List of current monarchs of sovereign states']
wikipedia.summary(query)


wikiurl="https://en.wikipedia.org/wiki/List_of_current_monarchs_of_sovereign_states"
table_class="wikitable sortable jquery-tablesorter"
response = requests.get(wikiurl)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.find('table',{'class':"wikitable"})

df = pd.read_html(str(indiatable))
df = pd.DataFrame(df[0])
print(df.head())

m_names = df[['Monarch (Birth year)', 'Title']]
m_names = m_names.rename(columns={"Monarch (Birth year)": "Name"})
m_names = m_names.replace("[\(\[].*?[\)\]]", "", regex=True)
m_names['Title'] = m_names['Title'].replace("Co-Princes", "Co-Prince", regex=True)

print(m_names)





