import requests
from bs4 import BeautifulSoup
url="https://www.flipkart.com/lenovo-loq-2024-intel-core-i5-13th-gen-13450hx-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-15irx9d2-gaming-laptop/p/itm52e42e03042c6?pid=COMGYSFGHPSWGZSV&lid=LSTCOMGYSFGHPSWGZSV3LJ4MP&marketplace=FLIPKART&store=4rr%2Ftz1&srno=b_1_1&otracker=browse&fm=organic&iid=en_iksYgdsFZ5wm7SD-yqUBhivblTFRI-GjZ1voCY-v6K2moQoZP41uo8IVttft0dAy36CR60rRnDArli6dU07RMPUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=nwmbr612mo0000001722865514932"
lap=requests.get(url)
htmlContent=lap.content
soup=BeautifulSoup(htmlContent,'html.parser')
page=soup.find_all(attrs={"class":"VU-ZEz"})
print(page)