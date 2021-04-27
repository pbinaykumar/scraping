from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

from gsheetapi import kickstarter

#forming a base URL
baseURL = "https://www.kickstarter.com/discover/advanced?sort=magic&seed=2699120&page="

options = Options()

#Using a fake user agent to avoid getting blocked by website. Need to dynamically rotate both user agent and IP to work better
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={userAgent}')
#Initializing the webdriver
driver = webdriver.Chrome(options=options)

list=[]
#looping over some sample URLs to parse data
for index in range(1, 10):
    #forming the final URL
    url = baseURL+str(index)

    #Calling the web page
    driver.get(url)
    # time.sleep(10)

    #Using try and exeption block to avoid termination of program due to some unexpected scenario
    try:
        #Initializing the soup parser to get HTML content
        soup = BeautifulSoup(driver.page_source, 'lxml') 

        #Finding titles and corresponding links with help of className
        titles = soup.find_all('h3',class_="type-18 light hover-item-text-underline mb1")
        links = soup.find_all('a',class_="soft-black mb3")
        #Printing the titles and links
        for item in range(len(titles)):
            print(titles[item].text, '....', links[item]['href'])
            list.append([titles[item].text,links[item]['href']])
        print(index)
        print("-----------------------------------------------------------------------------------------------------")

    except Exception as e:
        print(e)
        print("-----------------------------------------------------------------------------------------------------")

#Closing the web driver
# driver.close()
print(list)
for branchurl in list:
        driver.get(branchurl[1])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        print(soup)
        break