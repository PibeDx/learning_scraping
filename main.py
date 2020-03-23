from bs4 import BeautifulSoup
import requests

def filter_by_character_invalid(tag): 
  url = tag.get('href')
  if url != "" and url != "#" and url != "/":
    return True
  else:
    return False


def get_url(tag):
  return tag.get('href')


url = "https://boston.craigslist.org/search/sof"

response = requests.get(url)

print(response)

data = response.text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

#print(soup)

tags = soup.find_all('a')

filter_tags = filter(filter_by_character_invalid, tags)

urls = map(get_url, filter_tags)

for url in urls:
  print(url)

print(type(urls))
