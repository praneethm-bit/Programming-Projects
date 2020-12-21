#BeautifulSoup is responsible for parsing any web content
#requests is responsible for retreiving the web content
#pyttsx3 and engineio are together responsible for activating the text speaker here
from bs4 import BeautifulSoup
import requests
import pyttsx3
import engineio
#fetches the content of cnn world news
source = requests.get('https://www.cnn.com/world').text
#parses it through html
soup = BeautifulSoup(source, 'html5lib')
#finds all the headlines which are associated with this class
y = soup.find_all('span', class_ = 'cd__headline-text')
#activation of the text speaker
engine = pyttsx3.init()
#introduction to the news
engine.say('This is CNN and lets talk about what is happening around the world today.')
#speaks every news headline


source2 = requests.get('https://www.bbc.com/world').text

soup2 = BeautifulSoup(source2, 'html5lib')

a = soup2.find_all('h3', class_ = 'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

engine2 = pyttsx3.init()

for b in a:
    print(b.text)

