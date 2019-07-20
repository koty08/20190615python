from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title)

# print(soup.title.name)

# print(soup.a)
# print(soup.findAll('a'))

# a= soup.get_text()
# print(a)
# print(type(a))

# tag=soup.a
# # print(type(tag))
# # print(tag.name)
# # tag.name="blockquote"
# # print(tag.name)
# # print(soup)

# # tag['id']
# # print(tag.attrs)

# tag['id'] = 'verybold'
# tag['another-attribute']=1
# tag
# del tag['id']
# del tag['another-attribute']
# tag

# # print(tag['id'])
# print(tag.get('id'))
# print(soup)

# att1 = soup.a['class']
# print(att1)

# soup.a['class'] = ['sister', 'sis']
# att2=soup.a['class']
# print(att2)

# rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
# print(rel_soup.prettify())
# tag=rel_soup.a
# print(tag.string)
# print(type(tag.string))
# tag.string.replace_with('홈페이지')
# print(tag)

tag =soup.body
print(tag.contents[3])
print(len(tag.contents))

print(len(list(soup.children)))
print(len(list(soup.descendants)))
