# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Get the HTML
content = requests.get(url)
# htmlContent = r.content
htmlContent = content.content
# print(htmlContent)


# Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


# HTML Tree traversal
# objects -> 
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment


markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)
print(type(soup2.p.string))
# exit()
# Get the title of HTML page
title = soup.title

# Get all The Paragraphs of Html Page
paras =soup.find_all('p')
# print(paras)

# Get first element in the HTML page 
print(soup.find('p'))

# Get classesof any element in the HTML page 
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())  


# Get all The anchor tags of Html Page
anchors =soup.find_all('a')
all_links = set()

# print(anchors)
# Get all thr links on the page 
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linkText)



navbarSupportedContent = soup.find(id='navbarSupportedContent')
# for elem in navbarSupportedContent.children:
#     print(elem)
# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0] 
print(elem)