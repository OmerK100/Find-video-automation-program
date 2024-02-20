from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import time
import requests

from selenium_stealth import stealth



options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)


top_websites = {
    'Google': 'https://www.google.com',
    'YouTube': 'https://www.youtube.com',
    'Facebook': 'https://www.facebook.com',
    'Baidu': 'https://www.baidu.com',
    'Wikipedia': 'https://www.wikipedia.org',
    'Amazon': 'https://www.amazon.com',
    'Twitter': 'https://twitter.com',
    'Netflix': 'https://www.netflix.com',
    'Instagram': 'https://www.instagram.com',
    'LinkedIn': 'https://www.linkedin.com',
    'WhatsApp': 'https://www.whatsapp.com',
    'Microsoft': 'https://www.microsoft.com',
    'Tencent QQ': 'https://im.qq.com',
    'Yahoo': 'https://www.yahoo.com',
    'Taobao': 'https://www.taobao.com',
    'Zoom': 'https://zoom.us',
    'Pinterest': 'https://www.pinterest.com',
    'Reddit': 'https://www.reddit.com',
    'Tmall': 'https://www.tmall.com',
    'Alibaba': 'https://www.alibaba.com',
    'Snapchat': 'https://www.snapchat.com',
    'Weibo': 'https://www.weibo.com',
    'Booking.com': 'https://www.booking.com',
    'Google Maps': 'https://www.google.com/maps',
    'Microsoft Office 365': 'https://www.office.com',
    'WordPress': 'https://www.wordpress.org',
    'Naver': 'https://www.naver.com',
    'LINE': 'https://line.me',
    'Etsy': 'https://www.etsy.com',
    'Rakuten': 'https://www.rakuten.com',
    'XinhuaNet': 'http://www.xinhuanet.com',
    'Yahoo Japan': 'https://www.yahoo.co.jp',
    'Bing': 'https://www.bing.com',
    'Zillow': 'https://www.zillow.com',
    'BBC': 'https://www.bbc.com',
    'Apple': 'https://www.apple.com',
    'ESPN': 'https://www.espn.com',
    'CNN': 'https://www.cnn.com',
    'Yandex': 'https://www.yandex.ru',
    'MSN': 'https://www.msn.com',
    'Tumblr': 'https://www.tumblr.com',
    'Gmail': 'https://mail.google.com',
    'Quora': 'https://www.quora.com',
    'Sina Corp': 'https://www.sina.com.cn',
    'Outlook': 'https://outlook.live.com',
    'Flickr': 'https://www.flickr.com',
    'Ahrefs': 'https://ahrefs.com',
    'MSN China': 'http://www.msn.cn',
    'Dropbox': 'https://www.dropbox.com',
    'Spotify': 'https://www.spotify.com',
    'Minecraft': 'https://www.minecraft.net',
    'PayPal': 'https://www.paypal.com',
    'Adobe': 'https://www.adobe.com',
    'BBC News': 'https://www.bbc.co.uk/news',
    'Twitch': 'https://www.twitch.tv',
    'Sogou': 'https://www.sogou.com',
    'Booking Holdings': 'https://www.bookingholdings.com',
    'Craigslist': 'https://www.craigslist.org',
    'Samsung': 'https://www.samsung.com',
    'Hulu': 'https://www.hulu.com',
    'BBC Sport': 'https://www.bbc.com/sport',
    'Mail.ru Group': 'https://corp.mail.ru',
    'Oath Inc.': 'https://www.oath.com',
    'Chase Bank': 'https://www.chase.com',
    'Walmart': 'https://www.walmart.com',
    'IMDb': 'https://www.imdb.com',
    'Aol.com': 'https://www.aol.com',
    'Google Drive': 'https://drive.google.com',
    'Zalando': 'https://www.zalando.de',
    'Fox News': 'https://www.foxnews.com',
    'Elon Musk\'s Twitter': 'https://twitter.com/elonmusk'
}



browser = webdriver.Chrome(options=options)
#browser.get(top_websites.get(random.choice(list(top_websites.keys()))))
browser.get(top_websites.get("Google"))

search = browser.find_element(By.NAME, "q")

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

WORDS2 = []

for x in WORDS:
    WORDS2.append(x.decode("utf-8"))
    


word = random.choice(WORDS2)



search.send_keys(word)
search.send_keys("\n")

total_height = int(browser.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    browser.execute_script("window.scrollTo(0, {});".format(i))

#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")



#form = browser.find_element(By.TAG_NAME, "form")
#form.click()
#form.send_keys('test')

#search = browser.find_element(By.CLASS_NAME, "gNO89b")

#print(form)

