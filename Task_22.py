from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Task19:
   
   
   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def login(self):
      
       
       self.driver.maximize_window()
       self.driver.get(self.url)
       followers_count = self.driver.find_element(By.XPATH, '//span[@class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]').text
       print(f"Followers: {followers_count}")
       following_count = self.driver.find_element(By.XPATH, '//span[@class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]').text
       print(f"Following: {following_count}")

   def shutdown(self):
       self.driver.quit()




url = "https://www.instagram.com/guviofficial/"


task = Task19(url)
task.login()

task.shutdown()

