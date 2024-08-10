import requests
from bs4 import BeautifulSoup
url="https://www.youtube.com/watch?v=gDZ6czwuQ18"
lap=requests.get(url)
htmlContent=lap.content
soup=BeautifulSoup(htmlContent,'html.parser')
page=soup.find_all(attrs={"class":"content"})
print(page)