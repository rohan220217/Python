import requests
from bs4 import BeautifulSoup
url = "http://midas.iiitd.edu.in/"
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'lxml')


links = soup.find_all("a")
for link in links: 
    if "Research" in link.text:
        url2 = url + link.attrs['href']
        result2 = requests.get(url2)
        src2 = result2.content
        soup2 = BeautifulSoup(src2, 'lxml')
        images = soup2.find_all("img")
        for image in images:
            print(url2 + image['src'])









http://midas.iiitd.edu.in//projects//assets/themes/lab/images/logo/LOGO.png
http://midas.iiitd.edu.in//projects//assets/images/projects/multimodal-social-media.jpg
http://midas.iiitd.edu.in//projects//assets/images/projects/lipper.jpg
http://midas.iiitd.edu.in//projects//assets/images/projects/ai-healtcare.jpg
http://midas.iiitd.edu.in//projects//assets/images/projects/eventbuilder.jpg
http://midas.iiitd.edu.in//projects//assets/images/projects/code-switched-language.jpg
