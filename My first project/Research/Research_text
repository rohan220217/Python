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
        print(soup2.text)






Research


Toggle navigation












MIDAS@IIITD


Research
Team
Papers
Blog
Openings


              More 


News
Events










    Active Projects
  






Multimodal Social Media Analysis



In recent years, a huge amount of user-generated content (UGC) online (e.g., text, images, and videos) is accumulated on the web. UGC available on different platforms helps social media companies in sensing feedback, opinion, and interests of users, and provide services accordingly. However, due to the vast amount of data and inherent noise in social media content, often it is difficult to extract useful information from a single modality. Thus, it is essential to leverage information from multiple modalities to reduce noise from social media content. We leverage both multimedia content and contextual information to provide solutions to several important problems such as fake news detection, trolling detection, hate-speech detection, popularity predictions of photos, soundtrack recommendations for videos, and event summarization. At MIDAS@IIITD, we focus on building efficient fusion mechanisms using deep neural networks techniques which can help social media companies to provide a better service to their users. Our recent papers on multimodal social media analysis are published in top-tier conferences such as ACM Multimedia, WWW, NAACL, etc.









Lipreading and Speech Reconstruction



Speechreading broadly involves looking, perceiving, and interpreting spoken symbols. It has a wide range of multimedia applications, such as surveillance, Internet telephony, and as an aid to a person with hearing impairments. However, most of the work in speechreading has been limited to text generation from silent videos. Recently, research has ventured into generating (audio) speech from silent video sequences but there have been no developments in using multiple cameras for speech generation. To this end, this project encompasses the boundaries of multimedia research by putting forth a model which leverages silent video feeds from multiple cameras recording the same subject to generate intelligent speech for a speaker. Initial results confirm the usefulness of exploiting multiple views in building an efficient speech reading and reconstruction system. It further shows the optimal placement of cameras which would lead to the maximum intelligibility of speech. At MIDAS@IIITD, we plan to leverage the proposed system in various innovative applications and focus on its potential prodigious impact in not just security arena but in many other multimedia analytics problems. Our recent paper on speech reconstruction from silent videos is published in ACM Multimedia, a premier Multimedia conference.









Harnessing AI for Health Care



In recent years, advances in artificial intelligence techniques haveyielded immense success in computer vision, natural language processing, and speech processing. Healthcare is also one of the areas which got much benefited through this. Mining social media messages for health and drug-related information has received significant interest in pharmacovigilance research. For instance, an analysis of social media text (e.g., tweets, posts, and comments) using natural language processing and machine learning techniques helps in finding the adverse drug reactions, suicidal ideation, depression detection, medical information extraction, etc. Moreover, computer vision and machine learning techniques help the automatic detection of different disease from tissue images. For instance, it has shown immense success in the detection of cancer, diabetes, kidney failure, etc. Furthermore, speech processing in conjunction with artificial intelligence has shown great success in the treatment of people. Moreover, artificial intelligence helps in building systems for people with different abilities. At MIDAS@IIITD, we focus on several such interesting research problems (e.g., kidney glomeruli classification, automatic kidney fibrosis assessment, adverse drug reactions, and suicidal ideation ) leveraging deep learning techniques. Our recent papers in this area are published in top-tier conferences and journals such as IEEE Intelligent Systems, NAACL, etc.









Event Detection and Summarization



With the advent of smartphones and auto-uploaders, user-generated content (e.g., tweets, photos, and videos) uploads on social media have become more numerous and asynchronous. Thus, it is difficult and time taking for users to manually search (detect) interesting events. It requires for social media companies to automatically detect events and subsequently recommend them to their users. An automatic event detection is also very useful in an efficient search and retrieval of user-generated content. Furthermore, since the number of users and events on event-based social networks (EBSN) is increasing rapidly, it is not feasible for users to manually find the personalized events of their interest. We would like to further explore events on EBSN such as Meetup for different multimedia analytics projects such as recommending events, groups, and friends to users. At MIDAS@IIITD, we would like to use Deep Neural Network (DNN) technologies due to their immense success to address these interesting problems. Our recent papers on event detection and summarization are published in top-tier conferences and journals such as Knowledge-Based Systems, ACM Multimedia, ACM ICMR, etc.









Code-Switched Language Processing



The exponential rise of social media websites like Twitter, Facebook and Reddit in linguistically diverse geographical regions has led to hybridization of popular native languages with English in an effort to ease communication. For instance, Hinglish is formed of the words spoken in Hindi language but written in Roman script instead of the Devanagari script. It is a pronunciation based bi-lingual language that has no fixed grammar rules. Therefore, it is difficult to derive any useful information from such code-switched languages. Therefore, it necessitates social media companies to build models that can extract useful information from such languages. This will be useful in a number of applications such as detecting offensive languages, understanding feedback, opinions, and sentiments of users towards some product, news, events, policies, etc. At MIDAS@IIITD, we focus on building deep learning models which can extract useful information and automatically perform efficient classifications from code-switched languages such as Hinglish. For instance, our recent paper on detecting offensive language in Hinglish tweets is published in ACL, a premier NLP conference.










 









Indraprastha Institute of Information Technology, Delhi


About

Contact












