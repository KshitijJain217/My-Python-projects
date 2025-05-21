from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

# use if html.parser is not working
# soup = BeautifulSoup(contents, "lxml") # lxml is faster than html.parser
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)  # .string method, gets only the string inside the tag
# print(soup.prettify())

# print(soup.a) this will only return the first anchor tag

all_anchor_tags = soup.find_all(name="a")  # .find_all method, returns a list of all anchor tags
# print(all_anchor_tags) # returns a list of all anchor tags

for tag in all_anchor_tags:
    # print(tag.getText())  # .get method, gets the text inside the tag
    # print(tag.get("href"))  # .get() can get value of any attribute /  gets the href attribute of the tag
    pass

heading = soup.find(name="h1", id="name")  # .find method, returns the first h1 tag with id="name"
# print(heading)

# section_heading = soup.find(name="h3", class="heading")  # class is a reserved keyword in python, so use class_
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")  # inside selector tag values can be put same as in css,
# .select_one method, returns the first p tag with an anchor tag inside & .select, returns list of all items
# print(company_url)
name = soup.select_one(selector="#name")  # we can also select id and class
# print(name)
headings = soup.select(".heading")  # returns a list of all tags with class="heading"
print(headings)

