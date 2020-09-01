from selenium import webdriver
from bs4 import BeautifulSoup
import time


url = "https://10fastfingers.com/login"


browser = webdriver.Chrome()
browser.get(url)
time.sleep(20) # 10 seconds waiting to login



url = "https://10fastfingers.com/typing-test/english"
browser.get(url)
time.sleep(3) # 3 seconds waiting to load page source

html_source = browser.page_source
soup = BeautifulSoup(html_source,'html.parser')

wordsWithHtml = soup.find_all("div",attrs={"id":"row1"})

words = wordsWithHtml[0].getText().split()
del words[len(words)-1]

inputField = browser.find_element_by_xpath("//*[@id=\"inputfield\"]")
inputField.send_keys(wordsWithHtml[0].getText())

"""
for word in words:
    inputField.send_keys(word, " ")
    
"""