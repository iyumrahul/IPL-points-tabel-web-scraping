from bs4 import BeautifulSoup
#does not execute Javascript
response = requests.get(ipl_stats_url)
print(response.status_code)

with open('iplt20-stats.html', 'w') as f:
    f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

#find all the table tags
table_tag = doc.find('tr', class_='RR_0 np-bg-org').text
print(table_tag)