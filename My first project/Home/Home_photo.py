import requests
import json
from bs4 import BeautifulSoup 
result = requests.get("http://midas.iiitd.edu.in/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

images = soup.find_all("img")
for image in images:
    z = ( 'http://midas.iiitd.edu.in/' + image['src'])
    y = {"image":z}
    a = json.dumps(y)
    print(a)

    
{"image": "http://midas.iiitd.edu.in//assets/themes/lab/images/logo/LOGO.png"}
{"image": "http://midas.iiitd.edu.in//assets/themes/lab/images/banner/banner.jpeg"}
{"image": "http://midas.iiitd.edu.in//assets/themes/lab/images/banner/group_1.jpeg"}
{"image": "http://midas.iiitd.edu.in//assets/themes/lab/images/banner/group.jpeg"}
{"image": "http://midas.iiitd.edu.in//assets/themes/lab/images/banner/group_2.jpeg"}




