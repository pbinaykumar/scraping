from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from gsheetapi import indiegogo
#Base URL for Indiegogo
url = "https://www.indiegogo.com/explore/all?project_type=campaign&project_timing=all&sort=trending"

#Using a fake user agent to avoid getting blocked by website. Need to dynamically rotate both user agent and IP to work better
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={userAgent}')
#Initializing the webdriver
driver = webdriver.Chrome(options=options)
#Loading the web page
driver.get(url)
driver.implicitly_wait(15)

#Clicking show more button 10 times to load more no of products
# for _ in range(10):
#     js = "document.getElementsByClassName('i-cta-1 ng-binding ng-isolate-scope')[0].click();"
#     driver.execute_script(js)

#Sleeping for 10 seconds
# time.sleep(10)

#Getting title elements of all products
titles = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='discoverableCard-title ng-binding discoverableCard-lineClamp2']")))

#getting DIVs which contains the product page URL
LinkDivs = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='discoverableCard']")))
l1=[]
#Looping over the list of products
for i in range(len(LinkDivs)):
    #finding HTML source of the div which contains the product page URL
    htmlSource = LinkDivs[i].get_attribute('innerHTML')
    #Passing the HTML to BS4 soup object
    soup = BeautifulSoup(htmlSource, 'lxml') 
    #Finding the <a> tag
    links = soup.find_all('a')
    baseURL = 'https://www.indiegogo.com'
    #Forming the final URL by concatinating the base url and product page url
    product_URL = baseURL + links[0]["href"][:-5]+'#/'

    #finding the title of the page  
    product_title = titles[i].get_attribute('innerHTML')

    cat=soup.find_all('div',class_='discoverableCard-category ng-binding')[0].text.strip()

    #printing the product title and corresponding url
    print(product_title, '------->>', product_URL)
    l1.append([product_URL,cat])
l2=[]
for product_URL in l1:
    print('a')
    # time.sleep(10)
    print('b')
    branchurl = product_URL[0]
    driver.get(branchurl )
    soup = BeautifulSoup(driver.page_source, 'lxml')

    name=soup.find_all('div',class_='basicsSection-title is-hidden-tablet t-h3--sansSerif')[0].text.strip()
    address=soup.find_all('div',class_='basicsCampaignOwner-details-city')[0].text.strip()
    price=soup.find_all('span',class_='basicsGoalProgress-amountSold t-h5--sansSerif t-weight--bold')[0].text.strip()
    goal=soup.find_all('span',class_='basicsGoalProgress-progressDetails-detailsGoal-goalPercentageOrInitiallyRaised')[0].text.strip()
    if '%' in goal:
        goal=goal
    else:
        goal=''
    upco=soup.find_all('span',class_='tabHeadersWithPill-tab-pill t-label--sm')
    updates=upco[0].text.strip()
    comments=upco[1].text.strip()
    print(name)
    print(product_URL[0])
    print(address)
    print(price)
    print(goal)
    print(updates)
    print(comments)
    l2.append([name,product_URL[0],address,product_URL[1],'','','','','','','','','','',price,goal,'','',updates,comments])
print(l2)
indiegogo(l2)
# break
