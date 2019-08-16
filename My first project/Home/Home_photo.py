import requests
from bs4 import BeautifulSoup
result = requests.get("http://midas.iiitd.edu.in/")
src = result.content
soup = BeautifulSoup(src, 'lxml')


images = soup.find_all("img")
for image in images:
    print('http://midas.iiitd.edu.in/' + image['src'])




http://midas.iiitd.edu.in//assets/themes/lab/images/logo/LOGO.png
http://midas.iiitd.edu.in//assets/themes/lab/images/banner/banner.jpeg
http://midas.iiitd.edu.in//assets/themes/lab/images/banner/group_1.jpeg
http://midas.iiitd.edu.in//assets/themes/lab/images/banner/group.jpeg
http://midas.iiitd.edu.in//assets/themes/lab/images/banner/group_2.jpeg




