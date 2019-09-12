import requests 
import json
from bs4 import BeautifulSoup
import secrets
def save_img(i):
    with open(secrets.token_urlsafe()+". jpeg","wb") as f:
        f.write(requests.get(i["img"]). content)
URL="https://searchpy.herokuapp.com/images/search/?q="+input("enter query:")
headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
page= requests.get(URL, headers=headers)
soup= BeautifulSoup(page.content, "html.parser")
bing= soup.find(id="bing-data")
google= soup.find(id="google-data")
googledata= json.loads(google.text)
bingdata= json.loads(bing.text)
for i in googledata:
    save_img(i)
for i in bingdata:
    save_img(i)
      