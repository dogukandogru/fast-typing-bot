# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:29:00 2020

@author: dogru
"""

from selenium import webdriver
import time
import cv2
import pytesseract
import pyscreenshot as ImageGrab


url = "https://10fastfingers.com/login"
browser = webdriver.Chrome()
browser.get(url)


cont = ""
while True:
    cont = input()
    if(cont == "go"):
        break
    else:
        time.sleep(1)

startButton = browser.find_element_by_xpath("//*[@id=\"start-btn\"]")
startButton.click()

time.sleep(1.5)
img = ImageGrab.grab(bbox=(386, 416, 1115, 585))  # X1,Y1,X2,Y2
# save image file
img.save('ac.png')
        
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('ac.png')
text = pytesseract.image_to_string(img)
words = text.split()
inputField = browser.find_element_by_xpath("//*[@id=\"word-input\"]")

inputText = ""
for word in words:
    inputText = inputText + " " + word
    
inputField.send_keys(inputText)
time.sleep(0.2)
submitButton = browser.find_element_by_xpath("//*[@id=\"submit-anticheat\"]")
submitButton.click()