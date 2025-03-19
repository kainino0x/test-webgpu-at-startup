#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('chrome://gpu')
    body = driver.find_element(by=By.TAG_NAME, value='body')
    print(body.text)

while True:
    with webdriver.Chrome() as driver:
        driver.get('http://localhost:8083/')
        pre = driver.find_element(by=By.ID, value='pre')
        print(pre.text)
        driver.quit()
