import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


opts=webdriver.ChromeOptions()
opts.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install())

def scrape(url):
    driver.get(url)

    try:
      book_elements = driver.find_elements(By.XPATH, "//a[@class='a-link-normal a-text-normal']")
    except:
      return []

    with open('new_search_results.txt', 'a') as filehandle:
        for book in book_elements:
          book_link = book.get_attribute('href')
          print("book_link: " + book_link)
          if(book_link):
            filehandle.write('%s\n' % book_link)
    
with open("search_results_urls.txt",'r') as urllist:
    for url in urllist.read().splitlines():
        data = scrape(url)
    driver.quit()
