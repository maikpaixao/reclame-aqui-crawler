import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#driver = webdriver.Chrome(executable_path='C:/Users/paixo/Desktop/crawler/chromedriver.exe')
driver = webdriver.Firefox(executable_path='/home/maikpaixao/Downloads/geckodriver')
driver.set_window_size(1120, 800)

driver.get("https://www.reclameaqui.com.br/empresa/kanui/lista-reclamacoes/")
#text = driver.find_element_by_class_name("text-title").text
elements = driver.find_elements_by_css_selector("a.link-complain-id-complains")
texts = [elem.get_attribute('href') for elem in elements]

for text in texts[:2]:
  driver.get(text)
  doc = driver.find_element_by_css_selector("div.complain-body p").text
  print(doc)
  #driver.close()

driver.close()