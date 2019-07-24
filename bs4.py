import requests
from bs4 import BeautifulSoup

page_number = raw_input('Enter a page number to retreive information from: ')
r = requests.get("https://www.swiggy.com/udaipur?page="+str(page_number))
soup = BeautifulSoup(r.content)
name = []
cuisine = []
restaurant_information = []
for item in soup.find_all('div',{'class': 'nA6kb'}):
  name.append(item.text)
for item in soup.find_all('div',{'class': '_1gURR'}):
  item_info = item.text
  cuisine.append(item_info)
name_info = [str(i) for i in name]
cuisine_info = [str(i) for i in cuisine]
for restaurant_name,cusinie_type in zip(name_info, cuisine_info):
  restaurant_information.append([restaurant_name, cusinie_type])
restaurant_information