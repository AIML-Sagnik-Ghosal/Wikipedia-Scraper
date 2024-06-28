import requests
from bs4 import BeautifulSoup
import os
inp   = input("Enter Persons name: ")
#Searching in Google
link  = 'https://www.google.com/search?q=' + str(inp) +" "+ "Wikipedia"

link  = link.replace(' ','+')
res = requests.get(link)
soup  = BeautifulSoup(res.text,'html.parser')
for sp in soup.find_all('div'):
    try:
        link = sp.find('a').get('href')
        #Finding Wikipedia link
        if('en.wikipedia.org' in link):
            break
    except:
        pass
link = (link[7:]).split('&')[0]
link  = link.replace(' ','+')
paragraphs = ' '
#Scrapeing wikipedia link
re = requests.get(link)
soup = BeautifulSoup(re.text,'html.parser')
#List of all valid charecter
c=set([chr(i) for i in range(32,127)])
for i,p in enumerate(soup.find_all('p')):
    t=''''''
    for j in p.text:
        #Checking charecter is valid or not
        if j in c:
            t+=j
    paragraphs += t
    paragraphs += '\n'
    #Only 10 para is allowed
    if i>10:
        break
paragraphs = paragraphs.strip()
#File where we want to store our data
heading="C:\\Users\SAGNIK GHOSHAL\Documents\code\\phython\\information1.txt"
s=''
#Checking path already exist or not
if os.path.exists(heading):
    fd = open(heading , 'r')
    s=fd.read()
    fd.close()
#Adding To File
fd = open(heading, 'w',encoding='utf-8')
fd.write(inp+'\n'*3+paragraphs+'\n'*3+s)
fd.close()
print('done')