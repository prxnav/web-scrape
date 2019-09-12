import requests 
from bs4 import BeautifulSoup
URL='https://www.amazon.in/MSI-GS65-Stealth-9SF-635IN-i7-9750H/dp/B07Q9LQKL9/ref=sr_1_1?keywords=msi+g65+stealth&qid=1568221838&s=gateway&sr=8-1'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page = requests.get(URL, headers=headers)   
soup = BeautifulSoup( page.content, 'html.parser') 
title= soup.find(id="productTitle").get_text()
cost= soup.find(id="priceblock_ourprice").get_text()
converted_cost=cost[0:10]
print(title.strip())
print(converted_cost)
