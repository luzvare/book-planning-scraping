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


def get_book_name():
    try: 
       book_name = driver.find_element_by_id('productTitle').text
       to_return = '"' + book_name + '"'
       return to_return
    except: 
      return ""

def get_book_author():
    try:
       book_author = driver.find_element(By.XPATH, "//span[@class='author notFaded']/a").text
       to_return = '"' + book_author + '"'
       return to_return
    except: 
      return ""

def get_book_isbn_10():
    try: 
       book_isbn_10 = driver.find_element(By.XPATH, "//span[contains(text(), 'ISBN-10')]/following-sibling::span").text
       to_return = '"' + book_isbn_10 + '"'
       return to_return
    except: 
      return ""

def get_book_isbn_13():
    try: 
       book_isbn_13 = driver.find_element(By.XPATH, "//span[contains(text(), 'ISBN-13')]/following-sibling::span").text
       to_return = '"' + book_isbn_13 + '"'
       return to_return
    except: 
      return ""

def get_book_editorial():
    try: 
       book_editorial = driver.find_element(By.XPATH, "//span[contains(text(), 'Editorial')]/following-sibling::span").text
       to_return = '"' + book_editorial + '"'
       return to_return
    except: 
      return ""

def get_book_pages():
    try: 
       book_pages = driver.find_element(By.XPATH, "//span[contains(text(), 'Tapa')]/following-sibling::span").text
       to_return = '"' + book_pages + '"'
       return to_return
    except: 
      return ""

def get_book_image():
    try: 
       image_src = driver.find_element(By.XPATH, "//div[@id='img-canvas']/img").get_attribute('src')
       to_return = '"' + image_src + '"'
       return to_return
    except: 
      return ""

def scrape(url):
    driver.get(url)

    book_name = get_book_name()
    book_author = get_book_author()
    book_isbn_10 = get_book_isbn_10()
    book_isbn_13 = get_book_isbn_13()
    book_editorial = get_book_editorial()
    book_pages = get_book_pages()
    book_image = get_book_image()

    book_info = book_name + ',' + book_author + ',' + book_isbn_10 + ',' + book_isbn_13 + ',' + book_editorial + ',' + book_pages + ',' + book_image + '\n'
    return book_info
    
with open("new_search_results.txt",'r') as urllist, open('book_data.csv', 'a') as outputfile:
    headers = '"Nombre", "Autor", "ISBN-10", "ISBN-13", "Editorial", "Páginas", "Imagen"\n'
    outputfile.write(headers)
    for url in urllist.read().splitlines():
        try: 
          data = scrape(url)
          if(data != ',,,,,,\n'):
            print('escribiendo: ' + data)
            outputfile.write(data)
        except Exception as e:
            print(e)
    driver.quit()
    

