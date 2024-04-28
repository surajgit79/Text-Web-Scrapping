#web scrapping
from bs4 import BeautifulSoup
import requests

# extract the contents of the page
result = requests.get(url)
# print(result.status_code)

content = BeautifulSoup(result.text,"html.parser")
# print(content.prettify())

# Extract the heading first
H1 = content.find("h1",{"class":"alith_post_title"})
print(H1.text.strip())#strip function is used to remove unnecessary spaces

# Extract ythe heading second
H2 = content.find("h2",{"class":"alith_post_except animate-box"})
print(H2.text.strip())

# Extract the paragraphs
para = content.find_all("p")
for i in para:
    print(i.text)
    print()

# Placing in file:
with open ("scrap1.txt","w") as scarp1:
    scarp1.write(f"{H1.text.strip()}\n{H2.text.strip()}\n")
    '''scarp1.write()
    scarp1.write(H2.text.strip())'''
    for i in para:
        scarp1.write(f"{i.text}\n")


# demo url="https://thehimalayantimes.com/kathmandu/100-kg-gold-smuggled-out-of-tia-seized"