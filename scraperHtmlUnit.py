from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import sys
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

if(len(sys.argv) > 2):
    print("Aucun arguement détectéé")

chrome_options = Options()  
chrome_options.add_argument("--headless")  

browser = webdriver.Chrome('/Users/alcidefaucheron/Documents/Calendrier/chromedriver', chrome_options=chrome_options)

browser.get('https://vtmob.uphf.fr/esup-vtclient-up4/stylesheets/desktop/welcome.xhtml')

identifiant = '//*[@id="username"]'
mdp = '//*[@id="password"]'
connexion = '//*[@id="login"]/div[3]/input[6]'

calendrier = '//*[@id="j_id12"]/a[3]/img'

browser.find_element_by_xpath(identifiant).send_keys('afauch3_')
browser.find_element_by_xpath(mdp).send_keys(str(sys.argv[1]))
browser.find_element_by_xpath(connexion).click()
browser.find_element_by_xpath(calendrier).click()

time.sleep(2)

browser.close()