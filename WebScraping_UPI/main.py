import os, requests
from collections import OrderedDict
from bs4 import BeautifulSoup
import matplotlib.pylab as plt
os.system('clear')
page = requests.get('https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics')
#print(r.text)      # unicode
#print(r.content)   # bytes 
print(page.url, page.status_code)

txt = page.text     # full content
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text     # extract page title

page_body = soup.body # Extract page body (markup)
page_head = soup.head # Extract page head

first_h1 = soup.select('h1')[0].text # Extract first h1 text

# Create all_h3_tags as empty list
all_h3_tags = []
# Set all_h3_tags to all h3 tags of the soup
for element in soup.select('h3'):
    all_h3_tags.append(element.text)
str_h3 = ''.join(str(x) for x in all_h3_tags) # list to string
#print(all_h3_tags)

#link = soup.findAll("div", id="innerTabTwoJun22")
#print(link)

#table_div = soup.find('div', id='innerTabTwoJun22')
#table = table_div.find('tbody')
#print(table)

# data = soup.find_all("div", id ="innerTabTwoJun22")
# for i in data:
#     print(i)

# upi_table1 = soup.find('div', id="innerTabTwoJun22")  #working
# for apps in upi_table1.find_all('tbody'):
#     rows = apps.find_all('tr')
#     for row in rows:
#         name = row.find_all('td')[1].text.strip()
#         total = row.find_all('td')[11].text.strip()
#         print(name,total)

# d={}
# for tr in soup.findAll('tr'):
#     key = tr.text.split()[0]
#     val = tr.text.split()[1]
#     d[key] = val
#print(d)

# april 21 - jun 22

d = {}
upi_table1 = soup.find('div', id="innerTabTwoApr22")
for apps in upi_table1.find_all('tbody'):
    rows = apps.find_all('tr')
    for row in rows:
        name = row.find_all('td')[1].text.strip()
        total = row.find_all('td')[11].text.strip()
        total = total.replace(',', '')
        try:
            total = float(total)
        except ValueError:
            continue
        #print(name,total)
        d[name] = total

#d = OrderedDict(sorted(d.items(), key=itemgetter(1)))
d1 = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
#print(d1)

first_five = dict(zip(list(d1.keys())[:5], list(d1.values())[:5])) # first 5 elements
print(first_five)
myList = first_five.items()
#myList = sorted(myList) # sort keys
x, y = zip(*myList) # unpack a list of pairs into two tuples

plt.plot(x, y, marker='.', markersize=10, label="June 2022")
plt.xlabel('UPI apps')
plt.ylabel('Transactions Value (Cr)')
plt.title('upi-ecosystem-statistics')
plt.legend()
plt.xticks(rotation=10)
plt.show()