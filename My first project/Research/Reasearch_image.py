import requests
import json
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
            a = (url2 + image['src'])
            z = {"image": a}
            y = json.dumps(z)
            print(y)
{"image": "http://midas.iiitd.edu.in//projects//assets/themes/lab/images/logo/LOGO.png"}
{"image": "http://midas.iiitd.edu.in//projects//assets/images/projects/multimodal-social-media.jpg"}
{"image": "http://midas.iiitd.edu.in//projects//assets/images/projects/lipper.jpg"}
{"image": "http://midas.iiitd.edu.in//projects//assets/images/projects/ai-healtcare.jpg"}
{"image": "http://midas.iiitd.edu.in//projects//assets/images/projects/eventbuilder.jpg"}
{"image": "http://midas.iiitd.edu.in//projects//assets/images/projects/code-switched-language.jpg"}
