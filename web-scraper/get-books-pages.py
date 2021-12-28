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

opts=webdriver.ChromeOptions()
opts.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install())

def search_amazon(item):

    driver.get('https://www.amazon.com')
    search_box = driver.find_element_by_id('twotabsearchtextbox').send_keys(item)
    search_button = driver.find_element_by_id("nav-search-submit-text").click()

    driver.implicitly_wait(5)

    try:
        num_page = driver.find_element_by_xpath('//*[@class="a-pagination"]/li[6]')
    except NoSuchElementException:
        num_page = driver.find_element_by_class_name('a-last').click()

    driver.implicitly_wait(3)

    url_list = []

    for i in range(int(num_page.text)):
        page_ = i + 1
        url_list.append(driver.current_url)
        driver.implicitly_wait(4)
        click_next = driver.find_element_by_class_name('a-last').click()
        print("Page " + str(page_) + " grabbed")

    driver.quit()


    with open('search_results_urls.txt', 'w') as filehandle:
        for result_page in url_list:
            filehandle.write('%s\n' % result_page)

    print("---DONE---")

search_amazon('Libros de fantasía')
      