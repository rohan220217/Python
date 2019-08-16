import requests
from bs4 import BeautifulSoup
url = "http://midas.iiitd.edu.in/"
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'lxml')


links = soup.find_all("a")
for link in links: 
    if "Team" in link.text:
        url2 = url + link.attrs['href']
        result2 = requests.get(url2)
        src2 = result2.content
        soup2 = BeautifulSoup(src2, 'lxml')
        images = soup2.find_all("img")
        for image in images:
            print(url2 + image['src'])
            


http://midas.iiitd.edu.in//team//assets/themes/lab/images/logo/LOGO.png
http://midas.iiitd.edu.in//team//assets/images/team/rajiv.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/shivangi.png
http://midas.iiitd.edu.in//team//assets/images/team/hitkul.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/vaibhav.jpg
http://midas.iiitd.edu.in//team//assets/images/team/himani.jpg
http://midas.iiitd.edu.in//team//assets/images/team/prateekrawat.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/pallavi.jpg
http://midas.iiitd.edu.in//team//assets/images/team/himanshuaggarwal.jpg
http://midas.iiitd.edu.in//team//assets/images/team/shagun.jpg
http://midas.iiitd.edu.in//team//assets/images/team/midas_abhishek.jpg
http://midas.iiitd.edu.in//team//assets/images/team/Akash_pic.jpg
http://midas.iiitd.edu.in//team//assets/images/team/rajat-bansal.jpg
http://midas.iiitd.edu.in//team//assets/images/team/Dhruva-Sahrawat.jpg
http://midas.iiitd.edu.in//team//assets/images/team/vedant.JPG
http://midas.iiitd.edu.in//team//assets/images/team/osaid.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/harsh.png
http://midas.iiitd.edu.in//team//assets/images/team/mohits.jpg
http://midas.iiitd.edu.in//team//assets/images/team/RamaKrishna.jpg
http://midas.iiitd.edu.in//team//assets/images/team/mehak.jpg
http://midas.iiitd.edu.in//team//assets/images/team/hemant.jpg
http://midas.iiitd.edu.in//team//assets/images/team/imageKush.jpg
http://midas.iiitd.edu.in//team//assets/images/team/puneet.jpg
http://midas.iiitd.edu.in//team//assets/images/team/pic.jpg
http://midas.iiitd.edu.in//team//assets/images/team/Nilay.jpg
http://midas.iiitd.edu.in//team//assets/images/team/nupur-baghel.jpg
http://midas.iiitd.edu.in//team//assets/images/team/f2.jpg
http://midas.iiitd.edu.in//team//assets/images/team/shashwat-aggarwal.jpg
http://midas.iiitd.edu.in//team//assets/images/team/mansi-agarwal.png
http://midas.iiitd.edu.in//team//assets/images/team/Raghav_pic.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/apoorv_image.jpg
http://midas.iiitd.edu.in//team//assets/images/team/Namrata-Mukhija.JPG
http://midas.iiitd.edu.in//team//assets/images/team/anmol-chugh.jpg
http://midas.iiitd.edu.in//team//assets/images/team/arnav-arora.jpg
http://midas.iiitd.edu.in//team//assets/images/team/hritwik-dutta.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/karm.jpg
http://midas.iiitd.edu.in//team//assets/images/team/IMG_9517.jpg
http://midas.iiitd.edu.in//team//assets/images/team/yaman.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/simra.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/sarthak.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/salik.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/rohit.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/rajat.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/meghna.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/laiba.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/hitesh.jpeg
http://midas.iiitd.edu.in//team//assets/images/team/anjali.jpeg

