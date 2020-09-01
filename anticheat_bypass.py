# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:29:00 2020

@author: dogru
"""

from selenium import webdriver
import time
import cv2
import pytesseract



url = "https://10fastfingers.com"
browser = webdriver.Chrome()
browser.get(url)

cont = ""
while True:
    cont = input()
    if(cont == "go"):
        break
    else:
        time.sleep(1)

        
        
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('ac.png')
text = pytesseract.image_to_string(img)
words = text.split()
inputField = browser.find_element_by_xpath("//*[@id=\"word-input\"]")

for word in words:
    inputField.send_keys(word, " ")
    
submitButton = browser.find_element_by_xpath("//*[@id=\"submit-anticheat\"]")
submitButton.click()