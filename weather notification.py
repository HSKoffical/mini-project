import requests
import bs4
from plyer import notification
import time
def getdata(url):
    r = requests.get(url)
    return r.text
htmldata = getdata("https://weather.com/en-IN/weather/today/l/1224c80e65cdf058a59e3756ec505198834dc540c5976e75d1856e77426b27d9")

soup = bs4.BeautifulSoup(htmldata, 'html.parser')

# print(soup.prettify())
temp=soup.select("span.CurrentConditions--tempValue--MHmYY")
weather=soup.select(".CurrentConditions--phraseValue--mZC_p")
location=soup.select(".CurrentConditions--location--1YWj_")
message=" "
l1=[temp,weather,location]
for ele in l1:
    for value in ele:
        message=message+"\n "+str(value.text)




notification.notify(
            title="WEATHER",
            message=message,

            # displaying time
            timeout=10
        )
        # waiting time
time.sleep(7)

